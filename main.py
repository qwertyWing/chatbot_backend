from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 유저별 누적 메시지 저장
user_logs = {}

@app.post("/main")
def chat():
    user_id = request.headers.get("X-User-Id", "anonymous")
    data = request.get_json(silent=True) or {}
    msg = (data.get("message") or "").strip()
    if not msg:
        return jsonify({"reply": "(빈 입력)"}), 400

    # 유저별 누적
    history = user_logs.setdefault(user_id, [])
    history.append(msg)

    # 지금까지 받은 모든 메시지를 합쳐서 반환
    reply = "\n".join(history)
    return jsonify({"reply": reply})

@app.post("/reset")
def reset():
    user_id = request.headers.get("X-User-Id", "anonymous")
    user_logs.pop(user_id, None)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
