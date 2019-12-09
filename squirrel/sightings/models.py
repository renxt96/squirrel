from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    X = models.FloatField(
    )

    Y = models.FloatField(
    )

    unique_squirrel_id = models.CharField(
            max_length = 100,
    )

    PM = 'pm'
    AM = 'am'

    SHIFT_CHOICES = (
            (PM, 'PM'),
            (AM, 'AM'),
    )

    Shift = models.CharField(
            max_length = 5,
            choices = SHIFT_CHOICES,
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

    specific = models.CharField(
            max_length = 100,
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
    )

    chasing = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    climbing = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    eating = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    foraging = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    other_activities = models.CharField(
            max_length = 100
    )

    kuks = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    quaas = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    moans = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    tail_flags = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    tail_twitches = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )


    approaches = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    indifferent = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )

    runs_from = models.CharField(
            max_length = 20,
            choices = TF_CHOICES,
    )
