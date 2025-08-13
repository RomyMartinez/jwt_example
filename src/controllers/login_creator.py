from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.passord_handler import PasswordHandler
from typing import Dict, Tuple

class LoginCreator:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create_login(self, username: str, password: str) -> Dict:
        user = self.__get_user_by_username(username)
        user_id, username, hashed_password = user

        self.__validate_password(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        response = self.__format_response(token, username)
        return response

    def __get_user_by_username(self, username: str) -> Tuple[int, str, str]:
        user = self.__user_repository.get_user_by_username(username)
        if user is None:
            raise Exception("User not found")

        return user
    
    def __validate_password(self, password: str, hashed_password: str) -> None:
        is_password_valid = self.__password_handler.check_password(password, hashed_password)
        if not is_password_valid:
            raise Exception("Invalid password")
        
    def __create_jwt_token(self, user_id: int) -> str:
        payload = {
            "user_id": user_id
        }
        token = self.__jwt_handler.create_jwt_token(payload)
        return token

    def __format_response(self, token: str, username: str) -> Dict:
        return {
            "access_true": True,
            "username": username,
            "token": token
        }