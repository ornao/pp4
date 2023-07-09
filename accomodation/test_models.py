from django.test import TestCase

from .models import Accomodation


class AccomodationModelTest(TestCase):
    """ a class for accomodation model testing """
    @classmethod
    def setUp(self):
        self.accomodation = Accomodation(
            accomodation_type='Pod',
            accomodation_name='Pod Cupla', capacity=2, price_per_night=185.00)

    def test_accomodation_name_in_accomodation_model(self):
        """Checks accomodation model assigns accomodation_name"""
        self.assertEqual(self.accomodation.accomodation_name, 'Pod Cupla')

    def test_accomodation_type_in_accomodation_model(self):
        """Checks accomodation model assigns accomodation type"""
        self.assertEqual(self.accomodation.accomodation_type, 'Pod')

    def test_capacity_to_accomodation_model(self):
        """Checks accomodation model records capacity of accomodation"""
        self.assertEqual(self.accomodation.capacity, 2)

    def test_price_per_night_to_accomodation_model(self):
        """Checks accomodation model records price per night of accomodation"""
        self.assertEqual(self.accomodation.price_per_night, 185.00)
