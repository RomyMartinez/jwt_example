from src.drivers.jwt_handler import JwtHandler

def test_create_jwt_token():
    jwt_handler = JwtHandler()
    body = {"name": "John Doe"}

    token = jwt_handler.create_jwt_token(body)
    token_info = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)

    assert token_info["name"] == body["name"]
