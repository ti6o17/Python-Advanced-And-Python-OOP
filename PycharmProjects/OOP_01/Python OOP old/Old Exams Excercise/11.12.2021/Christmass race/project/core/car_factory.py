from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:

    valid_car_types_dict = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.valid_car_types_dict:
            return self.valid_car_types_dict[car_type](model, speed_limit)
        raise RuntimeError
