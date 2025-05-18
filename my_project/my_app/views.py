from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # names = ["Иван", "Мария", "Алексей"]
    names = []
    is_logged_in = True
    user_age = 25

    return render(
        request,
        "index.html",
        {
            "names": names,
            "is_logged_in": is_logged_in,
            "user_age": user_age,
        },
    )

def hello(request):
    return render(request, "hello.html")


def number(request, num):
    return HttpResponse(f"{num * 2}")


def hello_slug(request, slug):  # <-- добавляем новый маршрут
    return HttpResponse(f"Привет, {slug}!")
