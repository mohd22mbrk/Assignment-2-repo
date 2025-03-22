class GuestService:
    """Handles additional guest service requests."""

    def __init__(self, service_type):
        self.__service_type = service_type

    def request_service(self, guest):
        """Processes guest service requests."""
        return f"Service '{self.__service_type}' requested by {guest}."

    def __str__(self):
        return f"Service: {self.__service_type}"
