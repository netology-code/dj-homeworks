from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file = open('phones.csv', 'r')

        for index, line in enumerate(file):
            if index == 0:
                continue

            line = line.split(';')
            phone = Phone()
            phone.id = line[0]
            phone.name = line[1]
            phone.image = line[2]
            phone.price = line[3]
            phone.release_date = line[4]
            phone.lte_exists = line[5]
            phone.save()

        file.close()
