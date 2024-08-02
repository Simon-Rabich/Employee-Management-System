class InputError(Exception):
    """Exception raised for errors in the input."""
    def __init__(self, message="Invalid input. Please enter a valid number."):
        self.message = message
        super().__init__(self.message)
