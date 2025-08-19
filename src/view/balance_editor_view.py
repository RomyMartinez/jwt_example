from src.view.interfaces.view_interfaces import ViewInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.interfaces.balance_editor import BalanceEditorInterface

class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.headers.get("user_id")
        new_balance = http_request.body.get("new_balance")

        self.__validate_input(user_id, new_balance)

        response = self.__controller.edit_balance(user_id, new_balance)

        return HttpResponse(200, response)

    def __validate_input(self, user_id: any, new_balance: any) -> None:
        if user_id is None or new_balance is None:
            raise ValueError("Invalid input")

        if not isinstance(user_id, str) or not isinstance(new_balance, float):
            raise ValueError("Invalid input")