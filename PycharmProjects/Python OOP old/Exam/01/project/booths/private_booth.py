from project.booths.booth import Booth


class PrivateBooth(Booth):
    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        Booth.price_for_reservation = number_of_people * 3.5
        Booth.is_reserved = True
