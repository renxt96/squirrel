from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    longitude = models.FloatField(
            help_text=_('Longitude'),
     )

    latitude = models.FloatField(
            help_text=_('Latitude'),
     )

    unique_squirrel_id = models.CharField(
            help_text=_('Squirrel ID'),
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
            help_text=_('Shift'),
            max_length = 5,
            choices = SHIFT_CHOICES,
            default = AM,
    )


    date = models.DateField(
            help_text = _('Date'),
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
            help_text = _('Age'),
            max_length = 20,
            choices = AGE_CHOICES,
            default = ADULT,
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
            help_text = _('Primary Fur Color'),
            max_length = 20,
            choices = PRIMARY_FUR_COLOR_CHOICES,
            default = BLACK,
    )

    ABOVE_GROUND = 'above ground'
    GROUND_PLANE = 'ground plane'

    LOCATION_CHOICES = (
            (ABOVE_GROUND, 'Above Ground'),
            (GROUND_PLANE, 'Ground Plane'),
            (OTHER, 'N/A'),
    )

    location = models.CharField(
            help_text = _('Location'),
            max_length = 50,
            choices = LOCATION_CHOICES,
            default = ABOVE_GROUND,
    )

    specific_location = models.CharField(
            help_text = _('Specific Location'),
            max_length = 100,
    )

    TRUE = 'true'
    FALSE = 'false'

    TF_CHOICES = (
            (TRUE, 'True'),
            (FALSE, 'False'),
    )

    running = models.CharField(
            help_text = _('Running'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    chasing = models.CharField(
            help_text = _('Chasing'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    climbing = models.CharField(
            help_text = _('Climbing'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    eating = models.CharField(
            help_text = _('Eating'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    foraging = models.CharField(
            help_text = _('Foraging'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    other_activities = models.CharField(
            help_text = _('Other Activities'),
            max_length = 100
    )

    kuks = models.CharField(
            help_text = _('Kuks'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    quaas = models.CharField(
            help_text = _('Quaas'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    moans = models.CharField(
            help_text = _('Moans'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    tail_flags = models.CharField(
            help_text = _('Tail flags'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    tail_twitches = models.CharField(
            help_text = _('Tail twitches'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )


    approaches = models.CharField(
            help_text = _('Approaches'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    indifferent = models.CharField(
            help_text = _('Indifferent'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    runs_from = models.CharField(
            help_text = _('Runs from'),
            max_length = 20,
            choices = TF_CHOICES,
            default = FALSE,
    )

    def __str__(self):
        return self.unique_squirrel_id
