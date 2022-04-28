from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
from django.db.models import DecimalField
from django.urls import reverse


def only_letters_numbers_underscores_validator(value):
    for ch in value:
        if not (ch.isalnum() or ch=='_' or ch==' '):
            raise ValidationError('Value must contain only letters, numbers, underscores')


class Producer(models.Model):
    name = models.CharField(
        max_length=50,
    )
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Beer(models.Model):
    LAGER = 'Lager'
    STOUT = 'Stout'
    IPA = 'IPA'
    NON_ALCOHOL = 'Non alcohol'
    STYLES = [(x, x) for x in (LAGER, STOUT, IPA, NON_ALCOHOL)]

    brand = models.CharField(
        max_length=50,
        validators=(
            MinLengthValidator(2),
            only_letters_numbers_underscores_validator,
        )
    )

    style = models.CharField(
        max_length=max(len(x) for x, _ in STYLES),
        choices=STYLES,
        null=True,
        blank=True,
    )

    alc_volume = models.FloatField(
        validators=(
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ),
    )

    price = DecimalField(max_digits=4, decimal_places=2)

    label = models.ImageField(
        upload_to='beerlabels/',
        blank=True,
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('beer_details', args=[str(self.id)])


class Review(models.Model):
    beer = models.ForeignKey(
        Beer,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    review = models.TextField()

    def __str__(self):
        return self.review
