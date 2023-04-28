from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    VALID_HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __check_if_jockey_exists(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
            # return jockey

    def __check_if_horse_exists(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse
            # return horse

    def __check_if_horse_race_exists(self, race_type):
        for horse_race in self.horse_races:
            if race_type == horse_race.race_type:
                return horse_race

    def __check_if_horse_type_exists(self, horse_type):
        for i in range(len(self.horse_races), -1, -1):
            try:
                if self.horses[i].__class__.__name__ == horse_type:
                    return self.horses[i]
            except IndexError:
                raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__check_if_horse_exists(horse_name) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            horse_type_object = self.VALID_HORSE_TYPES[horse_type]
            self.horses.append(horse_type_object(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__check_if_jockey_exists(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__check_if_horse_race_exists(race_type) is not None:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = None
        if self.__check_if_jockey_exists(jockey_name) is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = self.__check_if_jockey_exists(jockey_name)
        if self.__check_if_horse_type_exists(horse_type):
            horse = self.__check_if_horse_type_exists(horse_type)
            if horse.is_taken:
                raise Exception(f"Horse breed {horse_type} could not be found!")
        if self.__check_if_jockey_exists(jockey_name) is not None:
            if jockey.horse is not None:
                return f"Jockey {jockey_name} already has a horse."
            jockey.horse = horse
            horse.taken = True
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        # jockey = None
        # horse_race = None
        if self.__check_if_horse_race_exists(race_type) is None:
            raise Exception(f"Race {race_type} could not be found!")
        horse_race = self.__check_if_horse_race_exists(race_type)
        if self.__check_if_jockey_exists(jockey_name) is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = self.__check_if_jockey_exists(jockey_name)
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        for horse_race in self.horse_races:

            for jockey in horse_race.jockey:
                if jockey.name == jockey_name:
                    return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockey.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        jockey_winner_name = None
        horse_winner_name = None
        if self.__check_if_horse_race_exists(race_type) is None:
            raise Exception(f"Race {race_type} could not be found!")
        horse_race = self.__check_if_horse_race_exists(race_type)
        if len(horse_race.jockey) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        jockey_max_speed = 0
        for jockey in horse_race.jockey:
            check_jockey_max_speed = max(jockey.horse.speed, jockey_max_speed)
            if check_jockey_max_speed > jockey_max_speed:
                jockey_max_speed = check_jockey_max_speed
                jockey_winner_name = jockey.name
                horse_winner_name = jockey.horse.name
        return f"The winner of the {race_type} race, with a speed of {jockey_max_speed}km/h is {jockey_winner_name}! Winner's horse: {horse_winner_name}."










