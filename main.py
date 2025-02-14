from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
CHAT_ID = "7689242465"
progress_log = []

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text")
    if message:
        if message == "/progress":
            send_message("\n".join(progress_log) if progress_log else "🔍 Καμία ενημέρωση προόδου ακόμα.")
        else:
            send_message(f"📩 Νέο μήνυμα: {message}")
    return {"status": "received"}

@app.route('/send_progress', methods=['GET'])
def send_progress():
    if progress_log:
        report = "\n".join(progress_log)
        send_message(f"📊 Αυτόματη ενημέρωση ({datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}):\n{report}")
    else:
        send_message("🔍 Δεν υπάρχουν νέες ενημερώσεις για το χρονικό διάστημα αυτό.")
    return {"status": "progress sent"}

def update_progress(update_msg):
    progress_log.append(update_msg)
    send_message(f"🔔 Ενημέρωση προόδου: {update_msg}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
