from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class BoothFactory:

    valid_booth_types_dict = {
        "OpenBooth": OpenBooth,
        "PrivateBooth": PrivateBooth
    }

    def create_booth(self, booth_type: str, booth_number: int,  capacity: int):
        if booth_type in self.valid_booth_types_dict:

            return self.valid_booth_types_dict[booth_type](booth_number, capacity)
        raise Exception(f"{booth_type} is not a valid booth!")

