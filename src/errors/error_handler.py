from .types.http_bad_request import HttpBadRequestError
from .types.http_unauthorized import HttpUnauthorizedError
from .types.http_not_found import HttpNotFoundError
from src.view.http_types.http_response import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpUnauthorizedError, HttpNotFoundError)):
        return HttpResponse(status_code=error.status_code, body={
          "name": error.name,
          "message": error.message,
        })
    
    return HttpResponse(status_code=500, body={
        "message": "Internal server error",
        "name": "InternalServerError"
    })