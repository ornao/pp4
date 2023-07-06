from django.test import TestCase

from .models import Testimonials, User, Accomodation


class TestimonialsModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.accomodation_name = Accomodation(
            accomodation_name='Honeymoon Pod')
        self.user = User(
            username='Sir Tester',
            )
        self.testimonials = Testimonials(
            accomodation_name=self.accomodation_name,
            author=self.user,
            rating=5,
            created_date='2023-07-01',
            )

    def test_username_in_user_model(self):
        """Checks testimonials model assigns user"""
        self.assertEqual(self.user.username, 'Sir Tester')

    def test_accomodation_name_in_accomodation_model(self):
        """Checks testimonials model assigns accomodation_name"""
        self.assertEqual(
            self.accomodation_name.accomodation_name, 'Honeymoon Pod')

    def test_created_date_in_testimonials_model(self):
        """Checks testimonials models assigns check in date"""
        self.assertEqual(self.testimonials.created_date, '2023-07-01')

    def test_rating_in_testimonials_model(self):
        """Checks testimonials models assigns check in date"""
        self.assertEqual(self.testimonials.rating, 5)

    def test_create_testimonials(self):
        """checks create testimonials is working correctly"""
        self.assertEqual(self.testimonials.author.username, 'Sir Tester')
        self.assertEqual(
                self.testimonials.accomodation_name, self.accomodation_name)
