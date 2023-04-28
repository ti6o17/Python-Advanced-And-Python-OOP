from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        Dessert.__init__(self, name, Cake.PRICE, Cake.CALORIES, Cake.CALORIES)
