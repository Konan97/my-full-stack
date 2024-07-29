from django.test import TestCase
from .models import Car
# Create your tests here.

class CarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Car = Car.objects.create(
            name = 'EX90',
            Rfid = 000000,
            ATACQ_Item = ""
        )
    
    def test_field(self):
        self.assertIsInstance(self.Car.Rfid, int)

        self.assertIsInstance(self.Car.name, int)