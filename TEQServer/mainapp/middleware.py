import traceback

from django.http import JsonResponse

class HandleExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            traceback.print_exc()

            return JsonResponse(
                {"detail": str(e)},
                status=400
            )