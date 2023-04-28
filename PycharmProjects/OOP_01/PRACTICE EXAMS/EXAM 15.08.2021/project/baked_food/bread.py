from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    portion = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion, price)

    def __repr__(self):
        ...
