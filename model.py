import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

with open("../model/tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)
with open("../model/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)
with open("../model/text_data.pkl", "rb") as f:
    text_data = pickle.load(f)

def is_valid_question(question):
    keywords = ["status", "health", "log", "device", "error", "update"]
    return any(k in question.lower() for k in keywords)

def get_answer_from_model(question, file_path):
    import pandas as pd

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        data = "\n".join(df.astype(str).apply(" | ".join, axis=1))
    else:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()

    lines = data.strip().split("\n")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(lines)
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, tfidf_matrix)
    best_match_index = similarities.argmax()
    return lines[best_match_index]

