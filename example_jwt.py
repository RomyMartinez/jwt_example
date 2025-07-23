from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route("/", methods=["POST"])
def first_function():
    return jsonify({"ola": "mundo"}), 200

@app.route("/login", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(minutes=1),
            "name": "John Doe",

        },
        key="secret",
        algorithm="HS256",
    )

    return jsonify({"token": token}), 200

@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split()[1]

    try:
        token = jwt.decode(token, key="secret", algorithms=["HS256"])
    except jwt.exceptions.ExpiredSignatureError as e:
        return jsonify({"errors": str(e)}), 401

    return jsonify({"message": token}), 200

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000, debug=True)
