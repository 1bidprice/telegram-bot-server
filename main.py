import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7706875882:AAHs0KLesc-vFNKG6sjoNq2dZlthJ5cMSF4"
CHAT_ID = "7689242465"  # Το δικό σου user ID

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text", "")
    if message:
        send_message(f"Έλαβε μήνυμα: {message}")
    return {"status": "received"}

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
