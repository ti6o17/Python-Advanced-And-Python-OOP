from project.car.car import Car
from project.car.sports_car import SportsCar
from project.car.muscle_car import MuscleCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    car_types = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def _if_car_model_exist_raise_exception(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                raise Exception(f"Car {car_model} is already created!")

    def _if_driver_exist_raise_exception(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

    def _if_race_exist_raise_exception(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar" or car_type == "SportsCar":
            # for car in self.cars:
            #     if car.model == model:
            #         raise Exception(f"Car {model} is already created!")
            self._if_car_model_exist_raise_exception(model)

            car = self.car_types[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        self._if_driver_exist_raise_exception(driver_name)
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        self._if_race_exist_raise_exception(race_name)
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def _take_last_car_type_in_cars(self, car_type):
        x = self.cars
        # y = self.cars[len(self.cars) - 1]
        reversed_cars = list(reversed(x))
        # for i in range(len(self.cars), -1, -1):
        #     if type(self.cars[0]) == car_type and not self.cars[0].is_taken:
        #         return self.cars[0]
        for car in reversed_cars:
            x = type(car).__name__
            y = car.is_taken
            if type(car).__name__ == car_type and not car.is_taken:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def _take_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        old_model = None
        driver = self._take_driver_by_name(driver_name)
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
        car = self._take_last_car_type_in_cars(car_type)
        driver.car = car
        car.is_taken = True
        if old_model is not None:
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        return f"Driver {driver_name} chose the car {car.model}."

    def _take_race_by_name(self, race_name):
        for race in self.races:
            x = race.name
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._take_race_by_name(race_name)
        driver = self._take_driver_by_name(driver_name)
        if driver.car is None:
            raise Exception("Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._take_race_by_name(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        # for driver in race.drivers:

        race_finish = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        race_finish[0].number_of_wins += 1
        race_finish[1].number_of_wins += 1
        race_finish[2].number_of_wins += 1
        result = f"Driver {race_finish[0].name} wins the {race_name} race with a speed of {race_finish[0].car.speed_limit}.\n"
        result += f"Driver {race_finish[1].name} wins the {race_name} race with a speed of {race_finish[1].car.speed_limit}.\n"
        result += f"Driver {race_finish[2].name} wins the {race_name} race with a speed of {race_finish[2].car.speed_limit}."
        return result





