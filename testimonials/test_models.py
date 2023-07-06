from django.test import TestCase

from .models import Testimonials, User, Accomodation


class TestimonialsModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.accomodation = Accomodation(
            accomodation_name='Honeymoon Pod')
        self.user = User(
            username='Sir Tester',
            )
        self.testimonials = Testimonials(
            accomodation_name=self.accomodation_name,
            author=self.user,
            num_guests=5,
            created_date='2023-07-01',
            )

    def test_username_in_testimonials_model(self):
        """Checks testimonials model assigns user"""
        self.assertEqual(self.user.username, 'Sir Tester')

    def test_accomodation_name_in_testimonials_model(self):
        """Checks testimonials model assigns accomodation_name"""
        self.assertEqual(
            self.accomodation_name.accomodation_name, 'Honeymoon Pod')

    def test_date_created_in_testimonials_model(self):
        """Checks testimonials models assigns check in date"""
        self.assertEqual(self.bookings.created_date, '2023-07-01')

    def test_max_rating_testimonials_model(self):
        """Checks bookings models assigns check in date"""
        self.assertEqual(self.bookings.created_date, '2023-07-01')
