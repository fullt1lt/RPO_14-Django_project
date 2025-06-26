from django.urls import path
from my_app.views import (
    home,
    hello,
    number,
    hello_slug,
    contact,
    ExampleViews,
    AboutViews,
    ProductsViews,
    ProductsDetailsViews,
    CreateProductViews,
    ProductsUpdateView,
    ProductsDeleteView,
    MyLoginViews,
    RegicterView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name="home_page"),
    path("hello/", hello, name="hello_page"),
    path("contact/", contact, name="contact_page"),
    path("number/<int:num>", number, name="number_page"),
    path("hello/slug/<slug:slug>/", hello_slug, name="hello_by_slug"),
    path("create_product/", CreateProductViews.as_view(), name="products_create"),
    path("register/", RegicterView.as_view(), name="register_page"),
    path("login/", MyLoginViews.as_view(), name="login_page"),
    path("logout/", LogoutView.as_view(next_page="home_page"), name="logout_page"),
    path("example/", ExampleViews.as_view(), name="example_page"),
    path("about/", AboutViews.as_view(), name="about_page"),
    path("products/", ProductsViews.as_view(), name="products_page"),
    path(
        "products/details/<int:pk>/",
        ProductsDetailsViews.as_view(),
        name="products_details_page",
    ),
    path(
        "products/update/<int:pk>",
        ProductsUpdateView.as_view(),
        name="products_update_page",
    ),
    path(
        "products/delete/<int:pk>",
        ProductsDeleteView.as_view(),
        name="products_delete_page",
    ),
]
