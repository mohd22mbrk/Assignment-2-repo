class Guest:
    """Represents a hotel guest with personal details and loyalty status."""

    def __init__(self, name, contact_info, loyalty_status="Regular"):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__reservation_history = []

    def create_account(self):
        """Creates a guest account."""
        return f"Account created for {self.__name}."

    def update_profile(self, name=None, contact_info=None):
        """Updates guest details."""
        if name:
            self.__name = name
        if contact_info:
            self.__contact_info = contact_info

    def add_reservation(self, booking):
        """Adds a booking to reservation history."""
        self.__reservation_history.append(booking)

    def __str__(self):
        return f"Guest: {self.__name}, Contact: {self.__contact_info}, Status: {self.__loyalty_status}"
