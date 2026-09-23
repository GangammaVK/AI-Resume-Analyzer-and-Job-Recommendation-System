import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_text_from_file
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import match_resume_to_jobs, get_role_gap
from roadmap_generator import generate_roadmap

from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

def create_analysis_pdf(filename, selected_role, results, gap, roadmap):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    styles["Title"].alignment = TA_CENTER
    story = [Paragraph("AI Resume Analyzer and Job Recommendation System", styles["Title"]), Spacer(1,12), Paragraph(f"<b>Resume:</b> {filename}", styles["BodyText"]), Paragraph(f"<b>Target Role:</b> {selected_role}", styles["BodyText"]), Spacer(1,10), Paragraph("Recommended Job Roles", styles["Heading2"])]
    data = [["Role", "Match Score (%)"]]
    for _, row in results.head(5).iterrows():
        data.append([str(row["role"]), f"{float(row['match_score']):.2f}"])
    table = Table(data, colWidths=[320,120])
    table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#17365D")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.5,colors.grey),("PADDING",(0,0),(-1,-1),6)]))
    story += [table, Spacer(1,12), Paragraph("Skills Found", styles["Heading2"]), Paragraph(", ".join(gap["found"]) if gap["found"] else "None", styles["BodyText"]), Spacer(1,8), Paragraph("Missing Skills", styles["Heading2"]), Paragraph(", ".join(gap["missing"]) if gap["missing"] else "None", styles["BodyText"]), Spacer(1,8), Paragraph("Learning Roadmap", styles["Heading2"])]
    if roadmap:
        for item in roadmap:
            story += [Paragraph(f"<b>{item['week']} — {item['topic']}</b>: {item['action']}", styles["BodyText"]), Spacer(1,5)]
    else:
        story.append(Paragraph("No roadmap items required.", styles["BodyText"]))
    story += [Spacer(1,12), Paragraph("Note: Match scores are estimates for educational guidance. They are not automatic hiring or rejection decisions.", styles["Italic"])]
    doc.build(story)
    return buffer.getvalue()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer and Job Recommendation System")
st.write(
    "Upload a resume to extract skills, compare it with job roles, "
    "identify skill gaps, and generate a simple learning roadmap."
)

with st.sidebar:
    st.header("Resume Upload")
    uploaded_file = st.file_uploader(
        "Choose a PDF or DOCX resume",
        type=["pdf", "docx"]
    )
    st.caption("Temporary processing only. Resumes are not permanently stored by this app.")

if not uploaded_file:
    st.info("Upload a PDF or DOCX resume to begin.")
    st.stop()

if uploaded_file.size > 5 * 1024 * 1024:
    st.error("File size is above the recommended 5 MB limit.")
    st.stop()

st.success(f"Uploaded: {uploaded_file.name}")

try:
    raw_text = extract_text_from_file(uploaded_file)
except Exception as exc:
    st.error(f"Could not read the resume: {exc}")
    st.stop()

if not raw_text.strip():
    st.error("No readable text was found in the resume.")
    st.stop()

cleaned = clean_text(raw_text)
skills = extract_skills(cleaned)
jobs = pd.read_csv("data/job_roles.csv")

results = match_resume_to_jobs(cleaned, skills, jobs)

left, right = st.columns(2)

with left:
    st.subheader("Extracted Skills")
    if skills:
        st.write(", ".join(sorted(skills)))
    else:
        st.warning("No skills from the current skill dictionary were detected.")

with right:
    st.subheader("Resume Text Preview")
    st.text_area("Cleaned text", cleaned[:6000], height=220)

st.subheader("Recommended Job Roles")
shown = results[["role", "match_score"]].copy()
shown["match_score"] = shown["match_score"].round(2)
st.dataframe(shown, use_container_width=True, hide_index=True)

fig = px.bar(
    results.head(5),
    x="match_score",
    y="role",
    orientation="h",
    title="Resume-to-Role Match Scores",
    labels={"match_score": "Match Score (%)", "role": "Job Role"}
)
fig.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig, use_container_width=True)

role_names = results["role"].tolist()
selected_role = st.selectbox("Select Target Role", role_names)

gap = get_role_gap(selected_role, skills, jobs)

c1, c2 = st.columns(2)
with c1:
    st.subheader("✅ Skills Found")
    st.write(", ".join(gap["found"]) if gap["found"] else "No required skills found.")

with c2:
    st.subheader("⚠️ Missing Skills")
    st.write(", ".join(gap["missing"]) if gap["missing"] else "No listed required skills are missing.")

st.subheader("Learning Roadmap")
roadmap = generate_roadmap(gap["missing"])
if roadmap:
    for item in roadmap:
        st.markdown(f"**{item['week']} — {item['topic']}**")
        st.write(item["action"])
else:
    st.success("No roadmap items are required for the selected role.")

st.subheader("Downloadable Analysis Report")
pdf_bytes = create_analysis_pdf(
    uploaded_file.name,
    selected_role,
    results,
    gap,
    roadmap
)
st.download_button(
    "📥 Download PDF Report",
    data=pdf_bytes,
    file_name="resume_analysis_report.pdf",
    mime="application/pdf"
)

st.divider()
st.caption(
    "Responsible AI: this is an educational guidance tool. Match scores are estimates, "
    "not automatic hiring or rejection decisions. The system does not score protected personal attributes."
)
