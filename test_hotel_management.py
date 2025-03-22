import unittest
from datetime import date
from guest import Guest
from room import Room
from booking import Booking
from payment import Payment
from loyalty import LoyaltyProgram
from guest_service import GuestService
from feedback import Feedback


class TestHotelManagementSystem(unittest.TestCase):

    def setUp(self):
        """Set up initial data for test cases."""
        self.guest1 = Guest("Alice Smith", "alice@example.com")
        self.guest2 = Guest("Bob Johnson", "bob@example.com")

        self.room1 = Room(101, "Single", ["Wi-Fi", "TV"], 100.0)
        self.room2 = Room(102, "Double", ["Wi-Fi", "TV", "Mini-bar"], 150.0)

        self.booking1 = Booking(1, self.guest1, self.room1, date(2025, 3, 25), date(2025, 3, 28))
        self.booking2 = Booking(2, self.guest2, self.room2, date(2025, 4, 10), date(2025, 4, 15))

    def test_guest_account_creation(self):
        """Test guest account creation and data storage."""
        self.assertEqual(self.guest1._Guest__name, "Alice Smith")
        self.assertEqual(self.guest1._Guest__contact_info, "alice@example.com")

    def test_search_available_rooms(self):
        """Test that available rooms can be searched correctly."""
        self.assertTrue(self.room1.check_availability())
        self.assertTrue(self.room2.check_availability())

    def test_make_room_reservation(self):
        """Test the reservation process and room availability update."""
        self.assertEqual(self.booking1.confirm_booking(), "Booking 1 confirmed for Alice Smith.")
        self.assertFalse(self.room1.check_availability())  # Room should be unavailable

    def test_booking_confirmation_notification(self):
        """Simulate a booking confirmation notification."""
        confirmation_message = self.booking2.confirm_booking()
        self.assertIn("Booking 2 confirmed for Bob Johnson.", confirmation_message)

    def test_invoice_generation(self):
        """Test invoice generation for a booking."""
        payment1 = Payment(101, self.booking1, self.booking1.calculate_total_price(), "Credit Card")
        self.assertIn("Invoice: Payment ID 101", payment1.generate_invoice())

    def test_payment_processing(self):
        """Test payment processing with different methods."""
        payment1 = Payment(102, self.booking1, self.booking1.calculate_total_price(), "Credit Card")
        payment2 = Payment(103, self.booking2, self.booking2.calculate_total_price(), "Mobile Wallet")

        self.assertIn("Credit Card", payment1.generate_invoice())
        self.assertIn("Mobile Wallet", payment2.generate_invoice())

    def test_display_reservation_history(self):
        """Test guest reservation history tracking."""
        self.booking1.confirm_booking()
        self.assertIn(self.booking1, self.guest1._Guest__reservation_history)

    def test_reservation_cancellation(self):
        """Test cancellation of a reservation and updating room availability."""
        self.booking1.confirm_booking()
        self.assertFalse(self.room1.check_availability())

        # Simulate cancellation by manually updating room availability
        self.room1._Room__availability = True
        self.assertTrue(self.room1.check_availability())

    def test_loyalty_program(self):
        """Test loyalty points accumulation and redemption."""
        loyalty = LoyaltyProgram()
        loyalty.add_points(self.guest1, 50)
        self.assertEqual(loyalty.redeem_points(self.guest1, 20), "20 points redeemed by Alice Smith.")

    def test_guest_service_request(self):
        """Test guest service request handling."""
        service1 = GuestService("Room Cleaning")
        request_message = service1.request_service(self.guest1)
        self.assertIn("Room Cleaning", request_message)

    def test_feedback_submission(self):
        """Test that guests can submit feedback."""
        feedback1 = Feedback(self.guest1, 5, "Excellent service!")
        self.assertIn("Excellent service!", feedback1.submit_feedback())


if __name__ == "__main__":
    unittest.main()
