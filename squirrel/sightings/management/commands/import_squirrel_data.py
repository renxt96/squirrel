from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import 2018 Central Park Squirrel Census Squirrel Data.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str, help='The CSV file to be imported')

    def handle(self,*args, **options):

        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            next(dataReader)

            for row in dataReader:
                S = Squirrel()

                try:
                    S.longitude = row[0]
                    S.latitude = row[1]
                    S.unique_squirrel_id = row[2]
                    S.shift = row[4]
                    S.date = dt.datetime.strptime(row[5],'%m%d%Y')
                    S.age = row[7]
                    S.primary_fur_color = row[8]
                    S.location = row[12]
                    S.specific_location = row[14]
                    S.running = row[15]
                    S.chasing = row[16]
                    S.climbing = row[17]
                    S.eating = row[18]
                    S.foraging = row[19]
                    S.other_activities = row[20]
                    S.kuks = row[21]
                    S.quuas = row[22]
                    S.moans = row[23]
                    S.tail_flags = row[24]
                    S.tail_twitches = row[25]
                    S.approaches = row[26]
                    S.indifferent = row[27]
                    S.runs_from = row[28]
                    #print('Enter Squirrel "%s"' % S.unique_squirrel_id)

                except:
                    pass

                S.save()
                #self.stdout.write(self.style.SUCCESS('Successfully import Squirrel "%s"' % S.unique_squirrel_id))
