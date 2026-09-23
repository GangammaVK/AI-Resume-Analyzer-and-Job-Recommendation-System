import re

def clean_text(text):
    if not text:
        return ""

    text = text.lower()

    # Preserve important technical tokens before removing punctuation.
    replacements = {
        "c++": "cpp",
        "c#": "csharp",
        ".net": "dotnet",
        "node.js": "nodejs",
        "react.js": "react",
        "next.js": "nextjs",
        "scikit-learn": "scikit learn",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"[^a-z0-9+#./_-]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()
