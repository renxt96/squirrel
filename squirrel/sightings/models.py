from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    longitude = models.FloatField(
        )

    latitude = models.FloatField(
        )

    unique_squirrel_id = models.CharField(
            max_length = 100,
            unique = True,
            primary_key = True,
        )

    PM = 'pm'
    AM = 'am'

    SHIFT_CHOICES = (
            (PM, 'PM'),
            (AM, 'AM'),
    )

    shift = models.CharField(
            max_length = 5,
            choices = SHIFT_CHOICES,
            default = AM,
    )


    date = models.DateField(
        )

    ADULT = 'adult'
    JUVENILE = 'juvenile'
    OTHER = ''

    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (OTHER, 'N/A'),
    )

    age = models.CharField(
            max_length = 20,
            choices = AGE_CHOICES,
            default = OTHER,
    )

    BLACK = 'black'
    GRAY = 'gray'
    CINNAMON = 'cinnamon'

    PRIMARY_FUR_COLOR_CHOICES = (
            (BLACK, 'Black'),
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (OTHER, 'N/A'),
    )

    primary_fur_color = models.CharField(
            max_length = 20,
            choices = PRIMARY_FUR_COLOR_CHOICES,
            default = OTHER,
    )

    ABOVE_GROUND = 'above ground'
    GROUND_PLANE = 'ground plane'

    LOCATION_CHOICES = (
            (ABOVE_GROUND, 'Above Ground'),
            (GROUND_PLANE, 'Ground Plane'),
            (OTHER, 'N/A'),
    )

    location = models.CharField(
            max_length = 50,
            choices = LOCATION_CHOICES,
            default = OTHER,
    )

    specific_location = models.CharField(
            max_length = 100,
            default = None,
            blank = True,
            null = True,
    )

    TRUE = 'true'
    FALSE = 'false'

    TF_CHOICES = (
            (TRUE, 'True'),
            (FALSE, 'False'),
    )

    running = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    chasing = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    climbing = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    eating = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    foraging = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    other_activities = models.CharField(
            max_length = 100,
            blank = True,
            null = True,
    )

    kuks = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    quaas = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    moans = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    tail_flags = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    tail_twitches = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )


    approaches = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    indifferent = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    runs_fro = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    def __str__(self):
        return self.unique_squirrel_id
