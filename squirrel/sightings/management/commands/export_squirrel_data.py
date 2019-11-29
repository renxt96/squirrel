from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
import datetime as dt


class Command(BaseCommand):
    help = 'Export 2018 Central Park Squirrel Census Squirrel Data.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to be exported')

    def handle(self,*args, **options):
        csv_file = options['csv_file']
        f = open(csv_file, 'w+')
        writer = csv.writer(f)
        field_names = [f.name for f in Squirrel._meta.fields]
        writer.writerow(field_names)

        for object in Squirrel.objects.all():
            row = [getattr(object, field) for field in field_names]
            writer.writerow(row)
        f.close()
