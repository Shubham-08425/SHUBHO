from flask import Flask, render_template, request, jsonify
import requests
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ✅ Load GROQ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ✅ Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Notes Page
@app.route('/notes')
def notes():
    return render_template('notes.html')

# ✅ Video Page
@app.route('/video')
def video():
    return render_template('video.html')

# ✅ MCQ / Objective Quiz Page
@app.route('/obj')
def obj():
    return render_template('obj.html')

# ✅ Doubts Page
@app.route('/doubts')
def doubts():
    return render_template('doubts.html')

# ✅ DPP Page
@app.route('/dpp')
def dpp():
    return render_template('dpp.html')

# ✅ PYQs Page
@app.route('/pyqs')
def pyqs():
    return render_template('pyqs.html')

# ✅ HOTS Page
@app.route('/hots')
def hots():
    return render_template('hots.html')

# ✅ Feedback Page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# ✅ Security Page
@app.route('/security')
def security():
    return render_template('security.html')

# ✅ Store Page
@app.route('/store')
def store():
    return render_template('store.html')

# ✅ NCERT Page
@app.route('/ncert')
def ncert():
    return render_template('ncert.html')

# ✅ Mind Map Page
@app.route('/mindmap')
def mindmap():
    return render_template('mindmap.html')

# ✅ AI Doubt Solver Endpoint
@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    user_question = data.get("question")

    if not user_question:
        return jsonify({"answer": "❌ No question received!"}), 400

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful tutor for class 10 students. Explain step by step in simple words."
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        data = response.json()
        ai_answer = data["choices"][0]["message"]["content"].strip()
        return jsonify({"answer": ai_answer})

    except Exception as e:
        return jsonify({"answer": f"⚠️ Error: {str(e)}"}), 500

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
