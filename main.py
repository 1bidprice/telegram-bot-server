import requests
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
CHAT_ID = "7689242465"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text", "")
    if message == "/progress":
        send_update()
    return {"status": "received"}

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def send_update():
    # Ενημέρωση για την πρόοδο των projects
    update_text = f"🔍 Ενημέρωση Προόδου ({datetime.now().strftime('%d-%m-%Y %H:%M')}):\n\n"
    update_text += "- 📈 Το **BidPrice** προχωρά κανονικά.\n"
    update_text += "- 🛒 Το **Project6225** βρίσκεται στο στάδιο ρύθμισης προμηθευτών.\n"
    update_text += "- ⚙️ Ρύθμιση υποδομών και βελτιστοποίηση κώδικα σε εξέλιξη.\n"
    send_message(update_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
