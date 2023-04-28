from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten



class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten=0, wing_size: float):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten=0, living_region: float):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

