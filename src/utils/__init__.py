from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


class ServiceUnvailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Update the structure of the response data.
    if response is not None:
        customized_response = {"success": False, "message": "request could not be processed", 'errors': []}

        for key, value in response.data.items():
            if isinstance(value, list):
                error = {'field': key, 'message': value}
            else:
                error = {'field': key, 'message': value}

            customized_response['errors'].append(error)

        response.data = customized_response

    return response

# def send_exc
