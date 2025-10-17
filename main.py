from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import defaultdict

app = Flask(__name__)
CORS(app)

# 유저별 누적 메시지 저장
user_logs = defaultdict(lambda: defaultdict(list))

MAX_ECHO = 50

@app.post("/main")
def chat():
    account_id = request.headers.get("X-Account-Id", "default")
    user_id = request.headers.get("X-User-Id", "anonymous")

    data = request.get_json(silent=True) or {}
    msg = (data.get("message") or "").strip()
    if not msg:
        return jsonify({"reply": "(빈 입력)"}), 400

    history = user_logs[account_id][user_id]
    history.append(msg)
    return jsonify({"reply": "\n".join(history[-40:])})

@app.post("/reset")
def reset():
    user_id = request.headers.get("X-User-Id", "anonymous")
    user_logs.pop(user_id, None)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
