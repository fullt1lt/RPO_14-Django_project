from django.urls import path
from my_app.views import home, hello, number, hello_slug

urlpatterns = [
    path("", home, name="home_page"),
    path("hello/", hello, name="hello_page"),
    path("number/<int:num>", number, name="number_page"),
    path("hello/slug/<slug:slug>/", hello_slug, name="hello_by_slug"),
]
