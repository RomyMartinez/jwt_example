from flask import Blueprint, jsonify

bank_account_routes = Blueprint("bank_account_routes", __name__)

@bank_account_routes.route("/bank_account", methods=["GET"])
def get_bank_account():
    return jsonify({"message": "Hello, World!"}), 200