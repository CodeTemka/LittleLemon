from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Test Dish", Price=9.99, Inventory=10)
        self.assertEqual(str(item), "Test Dish")