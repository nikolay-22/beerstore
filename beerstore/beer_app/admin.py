from django.contrib import admin

# Register your models here.
from beerstore.beer_app.models import Beer, Producer, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("brand", "producer", "price",)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass






