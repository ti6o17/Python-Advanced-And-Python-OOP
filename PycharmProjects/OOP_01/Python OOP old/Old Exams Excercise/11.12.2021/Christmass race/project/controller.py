from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        try:
            car = self.car_factory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."
        except RuntimeError:
            pass

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already created!"
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return f"Race {race_name} is already created!"
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # controller.add_car_to_driver("Peter", "SportsCar"))
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__find_last_free_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):

        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        return race.start()



    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_last_free_car_by_type(self, car_type):
        for idx in range(1, len(self.cars) + 1):
            car = self.cars[-idx]
            if not car.is_taken and type(car).__name__ == car_type:
                return car
        return None

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None


