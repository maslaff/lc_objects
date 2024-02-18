from django.core.management.base import BaseCommand
from app2_hw.models import Order, Product, User
from random import choices


class Command(BaseCommand):
    help = "Create orders."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            prods = set(choices(Product.objects.all(), k=4))
            total = sum([prod.price for prod in prods])
            order = Order(
                customer=user,
                total_price=total,
            )
            order.save()
            print(f"\n{order}\n\t{prods}")
            order.products.set(prods)

        self.stdout.write(f"{order}")
