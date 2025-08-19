from src.view.interfaces.view_interfaces import ViewInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.interfaces.login_creator import LoginCreatorInterface

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        self.__validate_input(username, password)

        response = self.__controller.create_login(username=username, password=password)
        return HttpResponse(200, response)

    def __validate_input(self, username: any, password: any) -> None:
        if username is None or password is None:
            raise ValueError("Invalid input")

        if not isinstance(username, str) or not isinstance(password, str):
            raise ValueError("Invalid input")