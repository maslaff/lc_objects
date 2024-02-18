from django.core.management.base import BaseCommand
from app2_hw.models import Product


class Command(BaseCommand):
    help = "Create test products."

    def handle(self, *args, **kwargs):
        for i in range(10):
            prod = Product(
                name=f"Product {i}",
                description=f"Weight: {(i+5)*(8+i)}",
                price=(i + 1) * 12,
                quantity=i * 2 + 4,
            )

            prod.save()
        self.stdout.write(f"{prod}")
