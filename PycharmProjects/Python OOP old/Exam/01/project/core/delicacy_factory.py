from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class DelicacyFactory:

    valid_delicacy_types_dict = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    def create_delicacy(self, delicacy_type: str, name: str, price: float):
        if delicacy_type in self.valid_delicacy_types_dict:
            return self.valid_delicacy_types_dict[delicacy_type](name, price)
        raise Exception(f"{delicacy_type} is not a valid booth!")
