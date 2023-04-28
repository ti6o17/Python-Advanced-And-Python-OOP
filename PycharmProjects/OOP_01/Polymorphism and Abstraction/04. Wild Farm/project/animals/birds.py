from project.animals.animal import Bird


class Owl(Bird):
    INCREASE_WEIGHT = 0.25
    ALLOWED_FOOD = ['Meat']

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if food.__class__.__name__ in Owl_food:
    #         self.weight += food.quantity * Owl.INCREASE_WEIGHT
    #         self.food_eaten += food.quantity
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    INCREASE_WEIGHT = 0.35
    ALLOWED_FOOD = ['Vegetable', 'Fruit', 'Meat', 'Seed']

    def make_sound(self):
        return 'Cluck'

    # def feed(self, food):
    #     if food.__class__.__name__ in Hen_food:
    #         self.weight += food.quantity * Hen.INCREASE_WEIGHT
    #         self.food_eaten += food.quantity
    #     return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

