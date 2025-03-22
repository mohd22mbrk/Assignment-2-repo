from datetime import date
from room import Room
from guest import Guest
from booking import Booking
from payment import Payment
from loyalty import LoyaltyProgram
from guest_service import GuestService
from feedback import Feedback

# Sample Data
guest1 = Guest("Alice Smith", "alice@example.com")
room1 = Room(101, "Single", ["Wi-Fi", "TV"], 100.0)

# Booking
booking1 = Booking(1, guest1, room1, date(2025, 3, 25), date(2025, 3, 28))
print(booking1.confirm_booking())

# Payment
payment1 = Payment(101, booking1, booking1.calculate_total_price(), "Credit Card")
print(payment1.generate_invoice())

# Loyalty Program
loyalty = LoyaltyProgram()
loyalty.add_points(guest1, 50)
print(loyalty.redeem_points(guest1, 20))

# Guest Service
service1 = GuestService("Room Service")
print(service1.request_service(guest1))

# Feedback
feedback1 = Feedback(guest1, 5, "Great stay!")
print(feedback1.submit_feedback())
