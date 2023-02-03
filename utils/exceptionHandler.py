from django.http import JsonResponse
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, NotAuthenticated
from http import HTTPStatus

STATUS_CODE_MAP = {
    500: "Server Error",
    400: "Bad Request",
    403: "Not Authorized",
    404: "Not Found",
}


def custom_exception_handler(exc, context):
    # Custom handler functions
    handlers = {
        "ValidationError": _handle_generic_error,
        "Http404": _handle_generic_error,
        "PermissionDenied": _handle_generic_error,
        "NotAuthenticated": _handle_authentication_error,
    }

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    """
    Exceptions can be raised as such also.
    
    if isinstance(exc, NotAuthenticated):
        custom_response_data = {
            'detail': 'Not Authenticated.'  # custom exception message
        }
        response.data = custom_response_data  # set the custom response data on response object

        return response
    """

    if response is not None:
        # Do whatever you want
        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            "error": {
                "status_code": 0,
                "custom_code": 0,
                "message": "",
                "details": [],
            }
        }
        error = error_payload["error"]
        status_code = response.status_code

        error["status_code"] = status_code
        error["custom_code"] = (
            STATUS_CODE_MAP[status_code]
            if status_code in STATUS_CODE_MAP
            else status_code
        )
        error["message"] = http_code_to_message[status_code]
        error["details"] = response.data
        response.data = error_payload

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_authentication_error(exc, context, response):
    response.data = {
        "error": "Please login to proceed",
        "status_code": response.status_code,
    }
    return response


def _handle_generic_error(exc, context, response):
    return response


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'Server Error (500)',
        "detail": "Custom Server Error Message"
    }
    return JsonResponse(data, status=500)


