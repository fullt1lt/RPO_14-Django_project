from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import FormContact, ProductForm, UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import IsAdminRequired

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from datetime import datetime
from django.contrib import messages 

def home(request):
    is_logged_in = False
    products = Product.objects.all()
    if request.user.is_authenticated:
        is_logged_in = True
    user = request.user.username if request.user.is_authenticated else "Гость"  # Получаем имя пользователя, если он аутентифицирован 
    return render(
        request,
        "index.html",
        {
            "products": products,
            "is_logged_in": is_logged_in,
            "user": user,  # Передаем имя пользователя в контекст
        },
    )

def hello(request):
    if request.method =="POST":
        name = request.POST.get("name") or "USER"
        return HttpResponse(f"ПРивет {name}")
    return render(request, "hello.html")


class ExampleViews(TemplateView):
    template_name = "example.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        color = self.request.COOKIES.get("color", "Белый")
        context["color"] = color
        return context

    def post(self, request, *args, **kwargs):
        color = request.POST.get("color")
        response = redirect(request.path)
        if color:
            response.set_cookie(key="color", value=color, max_age=3600)
        return response


class AboutViews(TemplateView):
    template_name = "about.html"
    extra_context = {"title": "О нас"}

# @method_decorator(cache_page(1), name='dispatch')
class ProductsViews(LoginRequiredMixin, ListView):
    template_name = "products.html"
    extra_context = {"title": "Продукты :))))))"}
    model = Product
    paginate_by = 5
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title2"] = "СИла чисел)))"
        context["category"] = Category.objects.all()
        context["date"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        product_id = self.request.session.get("product_id", [])
        try:
            context["product_cart"] = Product.objects.filter(id__in=product_id)
        except Product.DoesNotExist:
            context["product_cart"] = []
        return context

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        if product_id:
            carts_id = self.request.session.get("product_id", [])
            if product_id not in carts_id:
                carts_id.append(product_id)
                messages.success(request, "Товар добавлен в корзину!")
            messages.error(request, "Товар уже в корзине!")
            self.request.session["product_id"] = carts_id
        return redirect(request.path)


class ProductsDetailsViews(DetailView):
    template_name = "products_details.html"
    model = Product
    context_object_name = "product"


class CreateProductViews(IsAdminRequired,CreateView):
    template_name = "product_form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить новый товар!!!!!"
        return context


class ProductsUpdateView(UpdateView):
    template_name = "product_form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products_page")

class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products_page")


def number(request, num):
    product = Product.objects.get(id=num)  # Получаем всепродукты из базы данных
    return HttpResponse(f"{num * 2}")


def hello_slug(request, slug):  # <-- добавляем новый маршрут
    return HttpResponse(f"Привет, {slug}!")

def contact(request):
    if request.method =="POST":
        form = FormContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            return HttpResponse(f"Привет {name} - {email}")
    else:
        form = FormContact()
    return render(request, 'contacts.html', {"form": form})


class RegicterView(CreateView):
    template_name = "register.html"
    form_class = UserCreateForm
    model = User
    success_url = reverse_lazy("home_page")


class MyLoginViews(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home_page")
    redirect_authenticated_user = True
