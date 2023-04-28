class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):

        return  f"Player: {self.__name}\n" + \
                f"Sprint: {self.__sprint}\n" + \
                f"Dribble: {self.__dribble}\n" + \
                f"Passing: {self.__passing}\n" + \
                f"Shooting: {self.__shooting}"

"""	
You should create property only for the name of the player. The class should also have one additional method:
Override the __str__() method of the class so it returns:
"Player: {name}
Sprint: {sprint}
Dribble: {dribble}
Passing: {passing}
Shooting: {shooting}"

"""
