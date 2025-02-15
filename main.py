import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ρυθμίσεις Bot (Αντικατέστησε με δικές σου τιμές ή βάλε σε περιβάλλον .env)
TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"
CHAT_ID = "7689242465"

# Αρχική σελίδα για έλεγχο λειτουργίας
@app.route('/')
def home():
    return "Bot is running!", 200

# Webhook διαδρομή για Telegram και Cron-Job
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.json
        message = data.get("message", {}).get("text", "")
        sender = data.get("message", {}).get("from", {}).get("first_name", "Άγνωστος")

        if message:
            send_message(f"📩 Νέο μήνυμα από {sender}: {message}")
            if message == "/start":
                send_message("🚀 Το bot ξεκίνησε επιτυχώς!")
            elif message == "/progress":
                send_message("🔍 Καμία ενημέρωση προόδου ακόμα.")
            elif message == "/test_update":
                send_message("🛠️ Επιτυχής δοκιμή ενημέρωσης!")

    return jsonify({"status": "received"}), 200

# Keepalive διαδρομή για Cron-Job
@app.route('/keepalive', methods=['POST'])
def keepalive():
    send_message("🔔 Keepalive ping! Όλα λειτουργούν κανονικά.")
    return jsonify({"status": "alive"}), 200

# Συνάρτηση αποστολής μηνυμάτων μέσω του Telegram Bot API
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"⚠️ Αποτυχία αποστολής: {response.text}")
    except Exception as e:
        print(f"❌ Σφάλμα αποστολής: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
