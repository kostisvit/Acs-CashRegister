# your_app/middleware.py
import logging

logger = logging.getLogger(__name__)

class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Log the request information
        #logger.info(f"Method: {request.method}, Path: {request.path}, IP: {request.META['REMOTE_ADDR']}")

        # Log the response information
        logger.info(f"Status Code: {response.status_code}")

        return response
