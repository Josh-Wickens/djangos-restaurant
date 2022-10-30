from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .forms import ReserveTableForm
from booking_system.views import (DishList)


# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_menu_url(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func.view_class, DishList)
