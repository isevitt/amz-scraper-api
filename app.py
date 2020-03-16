from flask import Flask, request
from dbhelper import DBHelper
import sys

app = Flask(__name__)
DB = DBHelper()


@app.route("/start", methods=["GET", "POST"])
def insert_request_to_db():
    try:
        merchant_id = request.args.get("merchant_id")
        print(f"merchant id is {merchant_id}", file=sys.stdout)
        DB.add_input(merchant_id)
        return f"request was received for merchant id:  {merchant_id}"
    except Exception as e:
        return f"Error {e}"


if __name__ == '__main__':
    app.run(debug=True)


