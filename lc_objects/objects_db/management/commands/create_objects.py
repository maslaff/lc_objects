from django.core.management.base import BaseCommand
from objects_db.models import LCObjects, Organizations, Persons
from random import choice, choices, randint


class Command(BaseCommand):
    help = "Create test objects."

    def handle(self, *args, **kwargs):
        for i in range(10):
            obj = LCObjects(
                name=f"Большой {i}",
                address=f"ул. Первая, {(i+1)*2}",
                organization_id=choice(Organizations.objects.all()),
            )
            obj.save()
            obj.contact_person.set(choices(Persons.objects.all(), k=randint(1, 3)))
        self.stdout.write(f"{obj}")
