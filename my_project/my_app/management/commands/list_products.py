from django.core.management.base import BaseCommand
from my_app.models import Product  

class Command(BaseCommand):
    help = "Выводит спиок всех продуктов и их цены"

    def handle(self, *args, **kwargs):
        for product in Product.objects.all():
            self.stdout.write(f"{product.name} — {product.price} крон")
