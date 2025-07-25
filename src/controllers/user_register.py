from src.models.interfaces.user_repository import UserRepositoryInterface
from typing import Dict
from src.drivers.passord_handler import PasswordHandler

class UserRegister:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str) -> Dict:
        hashed_password = self.__create_hash_password(password)
        self.__registry_new_user(username, hashed_password)
        return self.__foramt_response(username)
        

    def __create_hash_password(self, password: str) -> str:
        hased_password = self.__password_handler.encrypt_password(password)
        return hased_password
    
    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)

    def __foramt_response(self, username: str) -> Dict:
        return {
            "type":"User",
            "count": 1,
            "username": username,
        }
    