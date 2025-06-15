from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import FormContact, ProductForm, LoginForm
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
    DeleteView,
)
from django.urls import reverse_lazy

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

class ExampleViews(View):
    http_method_names = ["get", "post"]  # Ограничиваем методы только GET и POST

    def get(self, request):
        return render(request, "example.html")

class AboutViews(TemplateView):
    template_name = "about.html"
    extra_context = {"title": "О нас"}

class ProductsViews(ListView):
    template_name = "products.html"
    extra_context = {"title": "Продукты :))))))"}
    model = Product
    paginate_by = 4
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title2"] = "СИла чисел)))"
        context["category"] = Category.objects.all()
        return context


class ProductsDetailsViews(DetailView):
    template_name = "products_details.html"
    model = Product
    context_object_name = "product"

class CreateProductViews(CreateView):
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


# @login_required
# def products_create(request):
#     if request.method == "POST":
#         category = Category.objects.get(id=1)
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.category = category
#             product.price += 100
#             form.save()
#             return redirect("home_page")
#     else:
#         form = ProductForm(initial={"price": 100, "name": "Без названия"})
#     return render(request, "product_form.html", {"form": form})


def regiester(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_views(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)  # сохраняем пользователя в сессии
            return redirect("home_page")  # редирект после логина
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_views(request):
    logout(request=request)
    return redirect("home_page")
