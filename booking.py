from datetime import date


class Booking:
    """Handles hotel bookings, linking guests and rooms."""

    def __init__(self, booking_id, guest, room, check_in, check_out):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """Calculates total stay cost."""
        days = (self.__check_out - self.__check_in).days
        return days * self.__room._Room__price_per_night

    def confirm_booking(self):
        """Confirms a room booking."""
        if self.__room.book_room():
            self.__guest.add_reservation(self)
            return f"Booking {self.__booking_id} confirmed for {self.__guest._Guest__name}."
        return "Booking failed. Room unavailable."

    def __str__(self):
        return f"Booking {self.__booking_id}: {self.__guest._Guest__name} from {self.__check_in} to {self.__check_out}"
