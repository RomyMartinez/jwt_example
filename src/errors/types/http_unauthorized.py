class HttpUnauthorizedError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 401
        self.message = message
        self.name = "Unauthorized"