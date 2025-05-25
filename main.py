from flask import Flask, request, jsonify
from tool_agent.agent import create_agent
import os

app = Flask(__name__)
agent = create_agent()

@app.route('/')
def home():
    return "Tool agent is running."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    result = agent.chat(user_input)
    return jsonify({"reply": result.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
