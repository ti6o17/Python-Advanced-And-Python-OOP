from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_decrease = mileage / self.MAX_MILEAGE
        self.MAX_MILEAGE -= self.MAX_MILEAGE * percentage_decrease
        self.battery_level -= round(percentage_decrease * 100)
