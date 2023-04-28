import unittest

from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):

    def test_init(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.assertEqual("Ivan", self.truck_driver.name)
        self.assertEqual(2, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_if_negative(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        with self.assertRaises(ValueError) as ex:
            self.truck_driver.earned_money = -2.1
        self.assertEqual(str(ex.exception), "Ivan went bankrupt.")

    def test_add_cargo_offer_raises_if_available(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.available_cargos = {"Varna": 400, "Sofia": 500}
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Varna", 400)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.available_cargos = {"Varna": 400, "Sofia": 500}
        added = self.truck_driver.add_cargo_offer("Ruse", 250)
        self.assertEqual(added, "Cargo for 250 to Ruse was added as an offer.")
        self.assertEqual(self.truck_driver.available_cargos, {"Varna": 400, "Sofia": 500, "Ruse": 250})

    def test_drive_best_cargo_offer_invalid(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer_valid(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.available_cargos = {"Varna": 400, "Sofia": 500, "Ruse": 250}
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, f"{self.truck_driver.name} is driving 500 to Sofia.")
        self.assertEqual(self.truck_driver.earned_money, 960)
        self.assertEqual(self.truck_driver.miles, 500)

    def check_eat(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.available_cargos = {"Varna": 400, "Sofia": 500, "Ruse": 250}

    def test_eat(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.earned_money = 100
        self.truck_driver.eat(250)
        self.truck_driver.eat(500)
        self.assertEqual(self.truck_driver.earned_money, 60)

    def test_sleep(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(self.truck_driver.earned_money, 10)

    def test_pump_gas(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.earned_money = 2000
        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)
        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repair_truck(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.truck_driver.earned_money = 16000
        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repr(self):
        self.truck_driver = TruckDriver("Ivan", 2)
        self.assertEqual(str(self.truck_driver), "Ivan has 0 miles behind his back.")

if __name__ == '__main__':
    unittest.main()