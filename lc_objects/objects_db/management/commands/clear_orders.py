from django.core.management.base import BaseCommand
from app2_hw.models import Order


class Command(BaseCommand):
    help = "Clear table."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all().delete()

        # order.save()

        self.stdout.write(f"Table orders cleared:\n{orders}")
