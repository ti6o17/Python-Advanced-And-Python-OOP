from unittest import TestCase


from project.vehicle import Vehicle


class TestVehicle(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    -
    def test_initialization(self):
        fuel = 100
        horse_power = 120

        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_car_drive_if_fuel_is_less(self):
        fuel = 100
        horse_power = 120

        vehicle = Vehicle(fuel, horse_power)
        with self.assertRaises(Exception) as error:
            vehicle.drive(81)
        self.assertEqual(100, vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_car_drive_reduces_fuel_when_distance_ok(self):
        fuel = 100
        horse_power = 120
        distance = 79

        vehicle = Vehicle(fuel, horse_power)

        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        vehicle.drive(distance)
        expected_result = fuel - fuel_needed
        self.assertEqual(expected_result, vehicle.fuel)

    def test_car_drive_with_maximum_distance(self):
        fuel = 100
        horse_power = 120
        distance = fuel/self.DEFAULT_FUEL_CONSUMPTION

        vehicle = Vehicle(fuel, horse_power)

        vehicle.drive(distance)
        expected_result = 0.0
        self.assertEqual(expected_result, vehicle.fuel)

    def test_refill_raises_error(self):
        fuel = 100
        horse_power = 120

        vehicle = Vehicle(fuel, horse_power)

        with self.assertRaises(Exception) as error:
            vehicle.refuel(10)
            self.assertEqual("Too much fuel", str(error.exception))

    def test_refill_after_travel(self):
        fuel = 100
        horse_power = 120

        vehicle = Vehicle(fuel, horse_power)
        vehicle.fuel -= 20
        vehicle.refuel(10)
        self.assertEqual(90, vehicle.fuel)

    def test_actual_str_returns_proper_string_message(self):
        fuel = 100
        horse_power = 120

        vehicle = Vehicle(fuel, horse_power)

        expected_result = f"The vehicle has {horse_power} horse power with {fuel} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected_result, str(vehicle))
"""
    def __str__(self):
        return f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"

"""


if __name__ == "__main__":
    main()