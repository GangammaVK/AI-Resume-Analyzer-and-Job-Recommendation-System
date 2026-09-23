# AI Resume Analyzer and Job Recommendation System

## Project Objective
This educational NLP-based application helps students understand how their resume matches selected job roles. It extracts resume text, identifies technical skills, compares the resume with job-role requirements, recommends roles, identifies missing skills, and generates a learning roadmap.

## Features
- Upload PDF or DOCX resume
- Extract text from PDF/DOCX
- Clean and normalize resume text
- Identify 20+ job-related skills using a controlled dictionary
- Compare resume with 7 job roles
- TF-IDF + cosine similarity matching
- Required-skill coverage calculation
- Top recommended roles
- Target-role skill-gap analysis
- Basic learning roadmap
- Interactive Streamlit dashboard
- Downloadable PDF analysis report
- Responsible-AI notice

## Folder Structure

```text
ai_resume_analyzer/
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
├── sample_resumes/
├── reports/
├── tests/
│   └── test_cases.csv
└── utils/
    ├── __init__.py
    └── helpers.py
```

## Setup in VS Code

### 1. Open the project folder
Open `ai_resume_analyzer` in VS Code.

### 2. Create a virtual environment

Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:
```powershell
venv\Scripts\activate.bat
```

### 3. Install packages
```powershell
pip install -r requirements.txt     
```

### 4. Run the project
```powershell
streamlit run app.py    
```

The Streamlit page will open in your browser.

## Matching Method
The project follows the beginner approach from the project guidance:
1. Extract resume text.
2. Clean and normalize text.
3. Detect skills using a controlled keyword dictionary.
4. Build TF-IDF vectors for the resume and job-role text.
5. Calculate cosine similarity.
6. Combine semantic similarity with required-skill coverage.
7. Sort job roles by the resulting match score.

### Match Score
The implementation uses:

`Match Score = 60% TF-IDF cosine similarity + 40% required-skill coverage`

This is an educational scoring formula, not a recruiter decision.

## Responsible AI
The application should be used for guidance, not automatic hiring or rejection. It does not intentionally score gender, age, religion, nationality, photograph, marital status, or disability. Missing keywords do not always mean missing ability.

## Testing
Run:
```powershell
python -m unittest discover tests -v
```

## Deployment
The project can be deployed using Streamlit Community Cloud, Render, or Docker after adding the appropriate deployment configuration.

## GitHub
Recommended commands:
```powershell
git init
git add .
git commit -m "Initial AI resume analyzer project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
