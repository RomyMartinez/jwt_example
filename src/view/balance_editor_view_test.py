import pytest
from src.view.balance_editor_view import BalanceEditorView
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from typing import Dict

class MockBalanceEditorController():
    def edit_balance(self, user_id: str, new_balance: float) -> Dict:
        return {
            "status": "success",
            "message": "Balance updated successfully"
        }

def test_handle():
    http_request = HttpRequest(headers={"user_id": "123"}, body={"new_balance": 100.0})
    expected_response = HttpResponse(200, {
        "status": "success",
        "message": "Balance updated successfully"
    })

    controller = MockBalanceEditorController()
    view = BalanceEditorView(controller)
    response = view.handle(http_request)

    assert response.body == expected_response.body

def test_handle_invalid_input():
    http_request = HttpRequest(headers={"user_id": "123"}, body={"new_balance": "100"})

    controller = MockBalanceEditorController()
    view = BalanceEditorView(controller)

    with pytest.raises(ValueError):
        view.handle(http_request)

def test_handle_missing_input():
    http_request = HttpRequest(headers={"user_id": "123"}, body={})

    controller = MockBalanceEditorController()
    view = BalanceEditorView(controller)

    with pytest.raises(ValueError):
        view.handle(http_request)
