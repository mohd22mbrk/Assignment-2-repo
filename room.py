class Room:
    """Represents a hotel room with details like type, amenities, price, and availability."""

    def __init__(self, room_number, room_type, amenities, price_per_night, availability=True):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__availability = availability

    def check_availability(self):
        """Returns room availability status."""
        return self.__availability

    def book_room(self):
        """Marks the room as unavailable."""
        if self.__availability:
            self.__availability = False
            return True
        return False

    def __str__(self):
        return f"Room {self.__room_number} ({self.__room_type}) - ${self.__price_per_night}/night"
