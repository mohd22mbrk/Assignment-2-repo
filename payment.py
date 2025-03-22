class Payment:
    """Handles payments and invoices for bookings."""

    def __init__(self, payment_id, booking, amount, payment_method):
        self.__payment_id = payment_id
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method

    def generate_invoice(self):
        """Generates an invoice for the booking."""
        return f"Invoice: Payment ID {self.__payment_id}, Amount: ${self.__amount}, Method: {self.__payment_method}"

    def __str__(self):
        return f"Payment {self.__payment_id}: ${self.__amount} via {self.__payment_method}"
