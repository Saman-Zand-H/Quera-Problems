from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from career.models import Company
import csv


class Command(BaseCommand):
    help = "export companies to csv"
    def handle(self, *args, **options):
        v = Company.objects.all().values_list("name", "email", "phone")
        with open(settings.BASE_DIR/"company.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for row in v:
                writer.writerow(row)