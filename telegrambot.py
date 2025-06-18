import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot is running!"

@app.route("/send")
def send_message():
    bot_token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    message = os.environ.get("MESSAGE", "Hello from Render!")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, data=payload)
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)