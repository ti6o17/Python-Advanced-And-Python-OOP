from project.core.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_out_of_range(value, 1, "Name should contain at least one character!")
        self.__name = value

    def start(self):
        race_winners = {}
        result = ''
        count = 0
        if len(self.drivers) < 3:
            raise Exception(f"Race {self.name} cannot start with less than 3 participants!")
        for driver in self.drivers:
            race_winners[driver.name] = driver.car.speed_limit
        sorted_race_winners = sorted(race_winners.items(), key=lambda x: x[1], reverse=True)[:3]
        for name, speed_limit in sorted_race_winners:
            for driver in self.drivers:
                if driver.name == name:
                    driver.number_of_wins += 1

            result += f'Driver {name} wins the {self.name} race with a speed of {speed_limit}.' + '\n'

        return result.strip()





