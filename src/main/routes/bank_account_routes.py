from flask import Blueprint, jsonify, request
from src.main.composer.user_register import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.balance_editor_composer import balance_editor_composer
from src.view.http_types.http_request import HttpRequest

bank_account_routes = Blueprint("bank_account_routes", __name__)

@bank_account_routes.route("/bank_account/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        view = user_register_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bank_account_routes.route("/bank_account/login", methods=["POST"])
def login_user():
    try:
        http_request = HttpRequest(body=request.json)
        view = login_creator_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bank_account_routes.route("/bank_account/balance/<user_id>", methods=["POST"])
def edit_balance(user_id):
    try:
        http_request = HttpRequest(body=request.json, params={"user_id": user_id})
        view = balance_editor_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500