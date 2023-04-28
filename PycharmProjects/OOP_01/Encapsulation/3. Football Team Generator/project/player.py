from unittest import result


class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        text_result = f'Player: {self.name}\n'
        text_result += f"Sprint: {self.__sprint}\n"
        text_result += f"Dribble: {self.__dribble}\n"
        text_result += f"Passing: {self.__passing}\n"
        text_result += f"Shooting: {self.__shooting}"
        return text_result
