from django.test import TestCase

from .models import Bookings, User, Accomodation

class BookingsModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.accomodation_name = Accomodation(accomodation_type='Pod', accomodation_name='Pod Almighty', capacity=5, price_per_night=185.00)
        self.user = User(
            username='Ms. Tester',
            email='test@email.com'
            )
        self.bookings = Bookings(
            booking_id=44,
            accomodation_name=self.accomodation_name,
            user=self.user,
            num_guests=5,
            created_date='2023-07-01',
            check_in_date='2023-07-13',
            check_out_date='2023-07-18',
            first_name='Test',
            last_name='Tester',
            email='test@email.com',
            )

    def test_username_in_user_model(self):
        """Checks user model assigns user"""
        self.assertEqual(self.user.username, 'Ms. Tester')

    def test_first_name_max_length(self):
        """Checks max length of first name field in bookings model"""
        max_length = Bookings._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):
        """Checks max length of last name field in bookings model"""
        max_length = Bookings._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_accomodation_name_in_accomodation_model(self):
        """Checks accomodation model assigns accomodation_name"""
        self.assertEqual(self.accomodation_name.accomodation_name, 'Pod Almighty')

    def test_check_in_date_in_bookings_model(self):
        """Checks bookings models assigns check in date"""
        self.assertEqual(self.bookings.check_in_date, '2023-07-13')

    def test_check_out_date_in_bookings_model(self):
        """Checks bookings models assigns check out date"""
        self.assertEqual(self.bookings.check_out_date, '2023-07-18')

    def test_add_number_guests_to_booking(self):
        """Checks bookings model records number of guests"""
        self.assertEqual(self.bookings.num_guests, 5)

    def test_create_booking(self):
        self.assertEqual(self.bookings.first_name, 'Test')
        self.assertEqual(self.bookings.last_name, 'Tester')
        self.assertEqual(self.bookings.booking_id, 44)
        self.assertEqual(self.bookings.check_in_date, '2023-07-13')
        self.assertEqual(self.bookings.check_out_date, '2023-07-18')
        self.assertEqual(self.bookings.num_guests, 5)
        self.assertEqual(self.bookings.email, 'test@email.com')
        self.assertEqual(self.bookings.accomodation_name, self.accomodation_name)