class S1mpleLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Этап до view
        print(f"[Middleware] Пришел запрос: {request.method} {request.path}")

        response = self.get_response(request)

        # Этап после view
        print(f"[Middleware] Ответ со статусом: {response.status_code}")
        return response
