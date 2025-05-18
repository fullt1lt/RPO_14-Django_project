from django.urls import path
from my_app.views import home, hello, number, hello_slug

urlpatterns = [
    path("", home),
    path("hello/<str:name>", hello),
    path("number/<int:num>", number),
    path("hello/slug/<slug:slug>/", hello_slug, name="hello_by_slug"),
]
