from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {'Gingerbread': Gingerbread,
                      'Stolen': Stolen}
    BOOTH_TYPES = {'Open Booth': OpenBooth,
                   'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        for delicacy in self.delicacies:
            if type(delicacy).__name__ not in self.DELICACY_TYPES:
                raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def _return_if_booth_has_enough_capacity_and_not_reserved(self, number_of_people):
        for booth in self.booths:
            x = booth.capacity
            y = booth.is_reserved
            if booth.capacity >= number_of_people and not booth.is_reserved:
                return booth
        raise Exception(f"No available booth for {number_of_people} people!")

    def reserve_booth(self, number_of_people: int):
        booth = self._return_if_booth_has_enough_capacity_and_not_reserved(number_of_people)
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def _returns_booth_with_provided_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        raise Exception(f"Could not find booth {booth_number}!")

    def _returns_delicacy_with_provided_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        raise f"No {delicacy_name} in the pastry shop!"

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._returns_booth_with_provided_number(booth_number)
        delicacy = self._returns_delicacy_with_provided_name(delicacy_name)

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._returns_booth_with_provided_number(booth_number)
        x = booth.price_for_reservation
        y = sum([delicacy.price for delicacy in booth.delicacy_orders])
        bill = booth.price_for_reservation + sum([delicacy.price for delicacy in booth.delicacy_orders])
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
