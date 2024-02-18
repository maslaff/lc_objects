from django.core.management.base import BaseCommand
from app2_hw.models import User


class Command(BaseCommand):
    help = "Create test Users."

    def handle(self, *args, **kwargs):
        for i in range(10):
            user = User(
                name=f"User {i}ovich",
                email=f"user{i}@post.ru",
                phone_number=f"+7987654321{i}",
                address=f"{90 - i*2} avenue st., {i*4}",
            )

            user.save()
        self.stdout.write(f"{user}")
