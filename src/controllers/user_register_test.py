from src.controllers.user_register import UserRegister

class MockUserRepository:
    def __init__(self):
        self.registry_user_attributes = {}
        
    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password

def test_user_register():
    user_repository = MockUserRepository()
    user_register = UserRegister(user_repository)

    username = "test"
    password = "test"

    response = user_register.registry(username, password)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["username"] == username

    assert user_repository.registry_user_attributes["username"] == username
    assert user_repository.registry_user_attributes["password"] is not None
    assert user_repository.registry_user_attributes["password"] != password