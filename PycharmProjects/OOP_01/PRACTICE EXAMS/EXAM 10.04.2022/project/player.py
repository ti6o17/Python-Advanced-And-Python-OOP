class Player:
    names = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        elif value in Player.names:
            raise Exception(f"Name {value} is already used!")
        Player.names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.__stamina < 100:
            return True

    # def __lt__(self, other):
    #     return self.stamina < other.stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina:.1f}, {self.need_sustenance}"
    


