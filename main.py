import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
CHAT_ID = "-4738149585"  # ID του group

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text")
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

@app.route('/send_update', methods=['GET'])
def send_update():
    update_text = "Καθημερινή ενημέρωση: Τα projects προχωρούν κανονικά!"
    send_message(update_text)
    return {"status": "update sent"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
