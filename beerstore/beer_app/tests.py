from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import request
from django.test import Client, TestCase
from django.urls import reverse

from .models import Beer, Producer, BeerDescription
from ..users.models import CustomUser

UserModel = get_user_model()

class BeerTests(TestCase):
    def setUp(self):
        self.producer = Producer.objects.create(
            name='Heineken',
            email='sales@heineken.com',
            website='www.heineken.com'
        )

        self.beerdescription = BeerDescription.objects.create(
            description="Some description",
        )

        self.beer = Beer.objects.create(
        brand ='Leffe Blond',
        style='Lager',
        alc_volume='4',
        price='3',
        label='',
        producer=self.producer,
        beerdescription=self.beerdescription,
        )


    def test_beer_listing(self):
        self.assertEqual(f'{self.beer.brand}', 'Leffe Blond')
        self.assertEqual(f'{self.beer.style}', 'Lager')
        self.assertEqual(f'{self.beer.alc_volume}', '4')
        self.assertEqual(f'{self.beer.price}', '3')
        self.assertEqual(f'{self.beer.label}', '')
        self.assertEqual(f'{self.beer.producer.name}', self.producer.name)
        self.assertEqual(f'{self.beer.beerdescription.description}', self.beerdescription.description)


    def test_create_beer_brand_contains_percent_sign_raises(self):
        beer = self.beer
        beer.brand = 'Leffe%'
        with self.assertRaises(ValidationError) as context:
            beer.full_clean()
            beer.save()
        self.assertIsNotNone(context.exception)


    def test_create_beer_brand_contains_less_than_two_characters_raises(self):
        beer = self.beer
        beer.brand = 'L'
        with self.assertRaises(ValidationError) as context:
            beer.full_clean()
            beer.save()
        self.assertIsNotNone(context.exception)


    def test_get__expect_correct_template(self):
        user_data = {
            'username': 'niki',
            'password': 'Passw0rd!',
        }
        CustomUser.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('beer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leffe Blond')
        self.assertTemplateUsed(response, 'beers/beer_list.html')


    def test_beer_detail_view(self):
        user_data = {
            'username': 'niki',
            'password': 'Passw0rd!',
        }
        CustomUser.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(self.beer.get_absolute_url())
        no_response = self.client.get('/beers/nonono/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Leffe Blond')
        self.assertTemplateUsed(response, 'beers/beer_details.html')




