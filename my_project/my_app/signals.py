from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase


@receiver(post_save, sender=Purchase)
def deduct_balance_after_purchase(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        print(
            f"[SIGNAL] Покупка совершена: {product.name} - {instance.purchased_at} (ID: {instance.id})"
        )
