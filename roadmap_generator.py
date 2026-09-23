ROADMAP = {
    "python": ("Python fundamentals", "Practice functions, lists, dictionaries, files, and small programs."),
    "sql": ("SQL", "Practice SELECT, JOIN, GROUP BY, subqueries, and basic database projects."),
    "excel": ("Excel", "Practice formulas, filtering, pivot tables, charts, and data cleaning."),
    "pandas": ("Pandas", "Practice DataFrame loading, cleaning, grouping, merging, and exporting."),
    "power bi": ("Power BI", "Build a dashboard using a small dataset and practice filters and measures."),
    "machine learning": ("Machine Learning", "Learn regression, classification, train/test split, metrics, and model evaluation."),
    "scikit learn": ("Scikit-learn", "Build a classification model and practice preprocessing and evaluation."),
    "fastapi": ("FastAPI", "Create a small REST API with validation and model prediction endpoints."),
    "docker": ("Docker", "Containerize a simple Python application and learn images, containers, and ports."),
    "deep learning": ("Deep Learning", "Learn neural networks, backpropagation, CNN basics, and training workflows."),
    "tensorflow": ("TensorFlow", "Build and train a small neural-network model and save/load it."),
    "keras": ("Keras", "Create a sequential model, train it, evaluate it, and inspect predictions."),
    "nlp": ("NLP", "Learn tokenization, text cleaning, TF-IDF, embeddings, and text classification."),
    "transformers": ("Transformers", "Understand attention and use a pretrained transformer for a small task."),
    "hugging face": ("Hugging Face", "Explore pretrained models, tokenizers, pipelines, and model fine-tuning basics."),
    "llm": ("LLMs", "Learn prompting, tokens, context windows, evaluation, and responsible use."),
    "rag": ("RAG", "Build a small retrieval pipeline using documents, embeddings, and generated answers."),
    "apis": ("REST APIs", "Practice HTTP methods, JSON, status codes, and consuming APIs from Python."),
    "opencv": ("OpenCV", "Practice image reading, resizing, color conversion, and basic computer vision."),
    "cnn": ("CNN", "Learn convolution, pooling, feature maps, and image classification."),
    "yolo": ("YOLO", "Learn object detection concepts and run a pretrained detector on sample images."),
    "mongodb": ("MongoDB", "Practice collections, documents, CRUD operations, and simple aggregation."),
    "mysql": ("MySQL", "Practice relational tables, keys, joins, and CRUD queries."),
    "postgresql": ("PostgreSQL", "Practice relational schema design, SQL queries, and transactions."),
    "sqlite": ("SQLite", "Build a small local application using tables and CRUD operations."),
    "git": ("Git", "Practice commits, branches, merge, pull, push, and basic conflict resolution."),
    "github": ("GitHub", "Create a repository, write a README, and use issues and pull requests."),
    "linux": ("Linux", "Practice navigation, files, permissions, processes, and common shell commands."),
    "aws": ("AWS basics", "Learn core compute, storage, networking, and deployment concepts."),
    "azure": ("Azure basics", "Learn core compute, storage, networking, and application deployment concepts."),
    "gcp": ("Google Cloud basics", "Learn core cloud services and basic application deployment concepts."),
    "cloud": ("Cloud deployment", "Deploy a small application and learn environment variables and logs."),
    "mlflow": ("MLflow", "Track experiments, metrics, artifacts, and model versions."),
    "kubernetes": ("Kubernetes", "Learn pods, deployments, services, and basic container orchestration."),
    "nodejs": ("Node.js", "Build a simple server and REST API with JavaScript."),
    "react": ("React", "Practice components, props, state, events, and API integration."),
    "angular": ("Angular", "Practice components, services, routing, forms, and API integration."),
    "flask": ("Flask", "Build a small web API with routes, request handling, and JSON responses."),
    "streamlit": ("Streamlit", "Create interactive data apps using widgets, charts, and session state."),
    "spaCy": ("spaCy", "Practice tokenization, named entities, phrase matching, and simple pipelines."),
    "nltk": ("NLTK", "Practice tokenization, stopwords, stemming, and basic text processing."),
}

def generate_roadmap(missing_skills):
    items = []
    for i, skill in enumerate(missing_skills[:8], start=1):
        key = skill.lower()
        if key in ROADMAP:
            topic, action = ROADMAP[key]
        else:
            topic = skill.title()
            action = f"Study the fundamentals of {skill} and build one small practical project."
        week = f"Week {i}"
        items.append({"week": week, "topic": topic, "action": action})
    return items
