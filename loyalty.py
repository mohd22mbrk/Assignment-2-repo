class LoyaltyProgram:
    """Manages guest loyalty points and rewards."""

    def __init__(self):
        self.__points = {}

    def add_points(self, guest, points):
        """Adds points to a guest's account."""
        self.__points[guest] = self.__points.get(guest, 0) + points

    def redeem_points(self, guest, points):
        """Redeems loyalty points."""
        if self.__points.get(guest, 0) >= points:
            self.__points[guest] -= points
            return f"{points} points redeemed by {guest._Guest__name}."
        return "Not enough points."

    def __str__(self):
        return "Loyalty Program Tracking System"
