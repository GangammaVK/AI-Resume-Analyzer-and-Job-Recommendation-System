import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _normalize_skill(skill):
    return skill.strip().lower()

def _required_skills(row):
    return [
        _normalize_skill(s)
        for s in str(row["required_skills"]).split("|")
        if s.strip()
    ]

def match_resume_to_jobs(resume_text, resume_skills, jobs):
    resume_skills_set = {_normalize_skill(s) for s in resume_skills}

    job_texts = jobs.apply(
        lambda row: f"{row['role']} {row['description']} {row['required_skills'].replace('|', ' ')}",
        axis=1
    ).tolist()

    corpus = [resume_text] + job_texts
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

    rows = []
    for idx, row in jobs.iterrows():
        required = _required_skills(row)
        found = len(set(required) & resume_skills_set)
        coverage = found / len(required) if required else 0.0

        # Balanced beginner-friendly score:
        # 60% semantic TF-IDF similarity + 40% required-skill coverage.
        score = (0.60 * float(similarities[idx]) + 0.40 * coverage) * 100

        rows.append({
            "role": row["role"],
            "match_score": round(score, 2),
            "skill_coverage": round(coverage * 100, 2),
            "required_skills": required
        })

    return pd.DataFrame(rows).sort_values(
        by="match_score", ascending=False
    ).reset_index(drop=True)

def get_role_gap(role, resume_skills, jobs):
    selected = jobs[jobs["role"].str.lower() == role.lower()]
    if selected.empty:
        raise ValueError(f"Role not found: {role}")

    required = _required_skills(selected.iloc[0])
    resume_set = {_normalize_skill(s) for s in resume_skills}

    found = sorted(set(required) & resume_set)
    missing = sorted(set(required) - resume_set)

    return {
        "role": role,
        "found": found,
        "missing": missing,
        "required": sorted(set(required))
    }
