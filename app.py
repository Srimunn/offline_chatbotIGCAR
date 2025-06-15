from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd

from model import is_valid_question, get_answer_from_model

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    file = request.files.get("file")
    question = request.form.get("question", "")

    if not file or not question:
        return jsonify({"answer": "No file or question provided"}), 400

    if not is_valid_question(question):
        return jsonify({"answer": "invalid question type, ask relevant to question for the uploaded file"}), 200

    # Save uploaded file (for logging or future extensions)
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    answer = get_answer_from_model(question, file_path)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
