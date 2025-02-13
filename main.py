import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
CHAT_ID = "-4738149585"  # Το δικό σου user ID

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text")
    chat_id = data.get("message", {}).get("chat", {}).get("id")

    if message:
        response = f"Έλαβα το μήνυμα: {message}"
        send_message(response, chat_id)
    return {"status": "received"}

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
