from flask import Flask, request
import datetime
import requests 

app = Flask(__name__)

@app.route("/start")
def send_scrape_request():
    merchant_id = request.args.get("merchant_id")
    resp = requests.get("https://www.google.com")
    return resp.text

if __name__ == '__main__':
    app.run(debug=True)
