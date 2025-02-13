import requests
from flask import Flask, request

app = Flask(__name__)

# Συμπλήρωσε με το δικό σου TOKEN
TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
# Το ID του group (από το getUpdates)
CHAT_ID = "-4738149585"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text")
    sender = data.get("message", {}).get("from", {}).get("first_name")
    if message:
        send_message(f"📩 Νέο μήνυμα από {sender}: {message}")
    return {"status": "received"}

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"❌ Error: {response.text}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
