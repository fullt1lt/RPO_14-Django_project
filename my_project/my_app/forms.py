from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from django.contrib.auth import authenticate

class FormContact(forms.Form):
    name = forms.CharField(label="Name", max_length=20)
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.startswith("d"):
            raise ValidationError("Ваш email начинается с буквы 'd'")
        return email

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "admin":
            self.add_error("name", "Недопустимое имя!!!")
            raise ValidationError("Ваше имя не может быть 'admin'")
        return name

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "photo"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 500:
            raise forms.ValidationError("Ценa меньше 500 крон!!!!!")
        return price

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        name = cleaned_data.get("name")
        if len(name) < 5 and price > 600:
            raise forms.ValidationError("Маленькое имя - большая цена!!!!")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Неверный логин или пароль")
        return cleaned_data
