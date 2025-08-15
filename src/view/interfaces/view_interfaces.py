from abc import ABC, abstractmethod
from src.view.http_request import HttpRequest
from src.view.http_response import HttpResponse

class ViewInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass