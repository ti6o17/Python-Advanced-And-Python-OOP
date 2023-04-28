from abc import ABC, abstractmethod


class Animal(ABC):
    INCREASE_WEIGHT = 0
    ALLOWED_FOOD = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += food.quantity * self.INCREASE_WEIGHT
            self.food_eaten += food.quantity
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]"

