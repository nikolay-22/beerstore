from django.db import models

# Create your models here.
from django.db.models import DecimalField
from django.urls import reverse


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

    brand = models.CharField(max_length=50)
    style = models.CharField(
        max_length=max(len(x) for x, _ in STYLES),
        choices=STYLES,
        null=True,
        blank=True,
    )
    alc_volume = models.FloatField()
    price = DecimalField(max_digits=4, decimal_places=2)
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('beer_details', args=[str(self.id)])


