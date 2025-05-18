from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    my_list = ['первый элемент', 'второй элемент', 'третий элемент', "3"]  # Список

    return render(request, 'index.html', {
        'my_list': my_list,
    })

def hello(request, name):
    return HttpResponse(f"Привет, {name}")


def number(request, num):
    return HttpResponse(f"{num * 2}")



def hello_slug(request, slug):  # <-- добавляем новый маршрут
    return HttpResponse(f"Привет, {slug}!")
