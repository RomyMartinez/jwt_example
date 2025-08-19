import pytest
from src.view.login_creator_view import LoginCreatorView
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class MockLoginCreatorController():
    def create_login(self, username: str, password: str) -> str:
        return {
          "status": "success",
          "message": "Login created successfully"
        }


def test_handle():
    http_request = HttpRequest(body={"username": "test", "password": "test"}) 
    expected_response = HttpResponse(200, {
        "status": "success",
        "message": "Login created successfully"
    })
    
    controller = MockLoginCreatorController()
    view = LoginCreatorView(controller)
    response = view.handle(http_request)

    assert response.body == expected_response.body

def test_handle_invalid_input():
    http_request = HttpRequest(body={"username": "test", "password": 123})

    controller = MockLoginCreatorController()
    view = LoginCreatorView(controller)

    with pytest.raises(ValueError):
        view.handle(http_request)

def test_handle_missing_input():
    http_request = HttpRequest(body={"username": "test"})

    controller = MockLoginCreatorController()
    view = LoginCreatorView(controller)

    with pytest.raises(ValueError):
        view.handle(http_request)
