from project.animals.animal import Animal, Mammal


class Mouse(Animal):
    INCREASE_WEIGHT = 0.1
    ALLOWED_FOOD = ['Vegetable', 'Fruit']

    def make_sound(self):
        return 'Squeak'


class Dog(Animal):
    INCREASE_WEIGHT = 0.4
    ALLOWED_FOOD = ['Meat']

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    INCREASE_WEIGHT = 0.3
    ALLOWED_FOOD = ['Vegetable', 'Meat']

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    INCREASE_WEIGHT = 1
    ALLOWED_FOOD = ['Meat']

    def make_sound(self):
        return 'ROAR!!!'



