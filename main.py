import requests
from flask import Flask, request

app = Flask(__name__)

# Ρυθμίσεις Bot
TOKEN = "7706875882:AAH5o7WQFV1mxLpt6TikdploTOr966dala8"  # Βάλε το δικό σου TOKEN
CHAT_ID = "7689242465"  # Το ID του Telegram group σου

# Αρχική σελίδα για έλεγχο λειτουργίας
@app.route('/')
def home():
    return "Bot is running!"

# Διαδρομή webhook για λήψη μηνυμάτων
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", {}).get("text", "")
    sender = data.get("message", {}).get("from", {}).get("first_name", "Άγνωστος")

    if message:
        # Απάντηση στο μήνυμα
        send_message(f"📩 Νέο μήνυμα από {sender}: {message}")

        # Ανταπόκριση σε συγκεκριμένες εντολές
        if message == "/start":
            send_message("🚀 Το bot ξεκίνησε επιτυχώς!")
        elif message == "/progress":
            send_message("🔍 Καμία ενημέρωση προόδου ακόμα.")
        elif message == "/test_update":
            send_message("🛠️ Επιτυχής δοκιμή ενημέρωσης!")
    
    return {"status": "received"}

# Διαδρομή για διατήρηση της υπηρεσίας "ζωντανής"
@app.route('/keepalive', methods=['GET'])
def keepalive():
    send_message("🔔 Έλεγχος keepalive. Είμαι εδώ!")
    return "I'm alive!", 200

# Συνάρτηση αποστολής μηνυμάτων μέσω του Telegram Bot API
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"⚠️ Αποτυχία αποστολής μηνύματος: {response.text}")
    except Exception as e:
        print(f"❌ Σφάλμα κατά την αποστολή μηνύματος: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
