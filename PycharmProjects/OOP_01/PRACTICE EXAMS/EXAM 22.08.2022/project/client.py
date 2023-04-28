class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        check_string = [num for num in value if num.isdigit()]
        if value[0] == 0 or len(value) == 10 or len(check_string) == 10:
            self.__phone_number = value
            return
        raise ValueError("Invalid phone number!")

