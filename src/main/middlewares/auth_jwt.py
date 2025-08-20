from flask import request
from src.view.http_types.http_request import HttpRequest
import src.drivers.jwt_handler as jwt_handler

def auth_jwt():
    jwt_handler = jwt_handler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise Exception("Token or user_id are required")

    token = raw_token.split()[1]
    token_info = jwt_handler.decode_jwt_token(token)
    token_user_id = token_info["user_id"]

    if user_id and token_user_id and (int(user_id) == int(token_user_id)):
      return token_info
    
    raise Exception("User not authenticated")