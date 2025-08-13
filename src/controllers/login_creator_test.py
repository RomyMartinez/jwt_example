from src.drivers.passord_handler import PasswordHandler
from src.controllers.login_creator import LoginCreator
from typing import Tuple
import pytest

username = "teste"
password = "123456"

password_handler = PasswordHandler()
hashed_password = password_handler.encrypt_password(password)

class MockUserRepository:
    def get_user_by_username(self, username: str) -> Tuple[int, str, str]:
        return (1, username, hashed_password)

def test_login_creator():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create_login(username, "123456")

    assert response["access_true"] is True
    assert response["username"] == username
    assert response["token"] is not None


def test_login_creator_invalid_password():
    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception) as e:
        login_creator.create_login(username, "1234567")
