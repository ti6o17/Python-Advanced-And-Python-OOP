from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, level_of_energy=25):
        super().__init__(name, level_of_energy)


