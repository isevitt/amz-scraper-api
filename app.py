from flask import Flask, request
import datetime
import requests 

app = Flask(__name__)

@app.route("/start")
def send_scrape_request():
    merchant_id = request.args.get("merchant_id")
    
    return f"request was sent for merchant id {merchant_id}, status code: {resp.status_code}" 

if __name__ == '__main__':
    app.run(debug=True)
