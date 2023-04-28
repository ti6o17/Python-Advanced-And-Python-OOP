from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str, level_of_energy=15):
        super().__init__(name, level_of_energy)
