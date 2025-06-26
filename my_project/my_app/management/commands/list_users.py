from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Выводит список всех пользователей"

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            self.stdout.write(f"{user.username} — {user.password}")
