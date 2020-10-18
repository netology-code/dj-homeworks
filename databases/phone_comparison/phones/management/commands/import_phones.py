import csv

from django.core.management.base import BaseCommand
from phones.models import Phone, UniqPhone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as isfile:

            phone_reader = csv.reader(isfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                res_ph = Phone(
                    brand=line[0], model=line[1], os=line[2], cam=line[3],
                    color=line[4], ram=line[5], proc=line[6], price=line[7]
                )
                res_uni = UniqPhone(
                    bt=line[8], wifi=line[9], sd=line[10]
                )
                res_ph.save()
                res_uni.save()
