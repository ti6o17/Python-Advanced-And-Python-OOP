
from project.booths.open_booth import OpenBooth
from project.core.booth_factory import BoothFactory
from project.core.delicacy_factory import DelicacyFactory


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def __check_if_delicacy_in_list(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                raise Exception(f"{delicacy_name} already exists!")
        return True

    def __check_if_booth_number_in_list(self, booth_number):
        for booth in self.booths:
            if booth.number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        return True
    delicacy_factory = DelicacyFactory()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.__check_if_delicacy_in_list(name):
            delicacy = self.delicacy_factory.create_delicacy(type_delicacy, name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    booth_factory = BoothFactory()

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__check_if_booth_number_in_list(booth_number):
            booth = self.booth_factory.create_booth(type_booth, booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.capacity == number_of_people:
                raise Exception(f"No available booth for {number_of_people} people!")
            type(booth).reserve(number_of_people)

            return f"Booth {booth.number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_bill = 0.0
        for booth in self.booths:
            if not booth.number == booth_number:
                raise Exception(f"Could not find booth {booth_number}!")
        for delicacy in self.delicacies:
            if not delicacy.name == delicacy_name:
                raise Exception(f"No {delicacy_name} in the pastry shop!")
            current_bill += delicacy.price
        self.income += current_bill

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        pass

    def get_income(self):
        pass
