
import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for ph in phones:
            # TODO: Добавьте сохранение модели
            slug = slugify(ph["name"])
            phone = Phone(name=ph["name"], image=ph["image"], price=ph["price"],
                          release_date=ph["release_date"], lte_exists=ph["lte_exists"],
                          slug=slug)
            phone.save()
