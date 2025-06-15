from django.urls import path
from my_app.views import (
    home,
    hello,
    number,
    hello_slug,
    contact,
    regiester,
    login_views,
    logout_views,
    ExampleViews,
    AboutViews,
    ProductsViews,
    ProductsDetailsViews,
    CreateProductViews,
    ProductsUpdateView,
    ProductsDeleteView,
)

urlpatterns = [
    path("", home, name="home_page"),
    path("hello/", hello, name="hello_page"),
    path("contact/", contact, name="contact_page"),
    path("number/<int:num>", number, name="number_page"),
    path("hello/slug/<slug:slug>/", hello_slug, name="hello_by_slug"),
    path("create_product/", CreateProductViews.as_view(), name="products_create"),
    path("register/", regiester, name="register_page"),
    path("login/", login_views, name="login_page"),
    path("logout/", logout_views, name="logout_page"),
    path("example/", ExampleViews.as_view(), name="example_page"),
    path("about/", AboutViews.as_view(), name="about_page"),
    path("products/", ProductsViews.as_view(), name="products_page"),
    path(
        "products/delete/<int:pk>/",
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
