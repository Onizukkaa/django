from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(choices=Genre.choices, max_length=5)
    genre = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    officila_homepage = models.fields.URLField(null=True, blank=True)



class Listing(models.Model):

    class Type(models.TextChoices):
        CLOTHING = "vêtements"
        POSTERS = "affiches"
        MISCELLANEOUS = "divers"


    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=2000, null=True)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    type = models.fields.CharField(choices=Type.choices, max_length=15, null=True)
