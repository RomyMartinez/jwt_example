from ast import Dict


class HttpRequest:
    def __init__(
        self, 
        body: Dict = None, 
        headers: Dict = None,
        token_info: Dict = None,
        params: Dict = None,
        ) -> None:
        self.body = body
        self.headers = headers
        self.token_info = token_info
        self.params = params

    