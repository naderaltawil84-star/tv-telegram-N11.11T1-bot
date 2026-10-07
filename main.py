import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    # استقبال النص المنسق قادماً من TradingView
    message_text = request.get_data(as_text=True)
    
    if message_text:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message_text,
            "parse_mode": "HTML"  # أو دعم التنسيق العادي
        }
        requests.post(url, json=payload)
        return "OK", 200
    return "No Data", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
