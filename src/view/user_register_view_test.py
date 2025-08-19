import pytest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.user_register_view import UserRegisterView

class MockUserRegisterController:
  def registry(self, username: str, password: str) -> str:
    return {
      "status": "success",
      "message": "User registered successfully"
    }

def test_user_register_view() -> None:
  body = {
    "username": "test",
    "password": "test"
  }

  request = HttpRequest(body=body)

  expected_response = HttpResponse(200, {
    "status": "success",
    "message": "User registered successfully"
  })

  controller = MockUserRegisterController()
  view = UserRegisterView(controller=controller)

  response = view.handle(request)

  assert isinstance(response, HttpResponse)
  assert response.status_code == 200
  assert response.body == expected_response.body

def test_user_register_view_invalid_input() -> None:
  body = {
    "username": 123,
    "password": 123
  }

  request = HttpRequest(body=body)

  controller = MockUserRegisterController()
  view = UserRegisterView(controller=controller)

  with pytest.raises(ValueError):
    view.handle(request)