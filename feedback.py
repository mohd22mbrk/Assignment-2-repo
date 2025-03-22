class Feedback:
    """Stores guest feedback and ratings."""

    def __init__(self, guest, rating, comments):
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments

    def submit_feedback(self):
        """Submits guest feedback."""
        return f"Feedback received from {self.__guest}: {self.__rating}/5 - {self.__comments}"

    def __str__(self):
        return f"Feedback: {self.__rating}/5 - {self.__comments}"
