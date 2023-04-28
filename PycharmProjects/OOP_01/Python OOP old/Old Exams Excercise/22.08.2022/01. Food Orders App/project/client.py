class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill: float = 0.0
        self.ordered_meals_quantity = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value[0] == "0" and not len(value) and not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value


