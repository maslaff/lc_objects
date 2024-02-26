from django.core.management.base import BaseCommand
from objects_db.models import Systems, LCObjects, SystemTypes
from random import choice, choices, randint


class Command(BaseCommand):
    help = "Create systems."

    def handle(self, *args, **kwargs):
        objs = LCObjects.objects.all()
        stypes = SystemTypes.objects.all()
        for obj in objs:
            for stype in choices(stypes, k=randint(1, len(stypes))):
                syst = Systems(
                    id_object=obj,
                    id_system_type=stype,
                    description=f"Эта система {randint(1, 100)} в {choice(['Сочи', 'Мире', 'России', 'Городе'])}",
                    documentation_path=f"lc_objects/media/{obj.name}",
                )
                syst.save()
        self.stdout.write(f"{syst}")
