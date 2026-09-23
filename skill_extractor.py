import re
from collections import OrderedDict

# Controlled skill dictionary. This is intentionally transparent and editable.
SKILL_CATEGORIES = OrderedDict({
    "Programming": [
        "python", "java", "javascript", "typescript", "cpp", "csharp",
        "html", "css", "sql", "php", "r"
    ],
    "Web": [
        "react", "angular", "vue", "nodejs", "express", "django", "flask",
        "fastapi", "nextjs", "rest api", "apis"
    ],
    "Data": [
        "pandas", "numpy", "excel", "power bi", "tableau", "matplotlib",
        "plotly", "data analysis", "statistics"
    ],
    "Machine Learning": [
        "machine learning", "scikit learn", "tensorflow", "keras",
        "pytorch", "deep learning", "cnn", "computer vision", "nlp",
        "natural language processing", "transformers", "hugging face",
        "llm", "rag", "yolo"
    ],
    "Database": [
        "mysql", "postgresql", "mongodb", "sqlite", "redis"
    ],
    "Cloud and DevOps": [
        "docker", "aws", "azure", "gcp", "cloud", "mlflow", "git", "github",
        "linux", "kubernetes"
    ],
    "Tools": [
        "opencv", "jupyter", "streamlit", "spaCy", "nltk"
    ]
})

SKILL_ALIASES = {
    "scikit-learn": "scikit learn",
    "scikit-learn": "scikit learn",
    "node.js": "nodejs",
    "react.js": "react",
    "natural language processing": "nlp",
    "spacy": "spaCy",
}

def extract_skills(text):
    text_lower = text.lower()
    found = []

    for category_skills in SKILL_CATEGORIES.values():
        for skill in category_skills:
            pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
            if re.search(pattern, text_lower):
                found.append(SKILL_ALIASES.get(skill, skill))

    return sorted(set(found))

def skills_by_category(skills):
    output = {}
    skill_set = set(skills)
    for category, values in SKILL_CATEGORIES.items():
        matched = [s for s in values if SKILL_ALIASES.get(s, s) in skill_set or s in skill_set]
        if matched:
            output[category] = sorted(set(SKILL_ALIASES.get(s, s) for s in matched))
    return output
