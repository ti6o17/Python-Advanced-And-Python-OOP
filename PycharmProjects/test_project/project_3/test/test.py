from project.robot import Robot

import unittest

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot('123', 'Military', 10, 3500)

    def test_init_robot(self):
        self.assertEqual(self.robot.robot_id, "123")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(self.robot.price, 3500)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_init_robot_category_raises(self):
        with self.assertRaises(ValueError) as va:
            self.robot = Robot('123', 'Home', 10, 3500)
        self.assertEqual(str(va.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_init_robot_price_raises(self):
        with self.assertRaises(ValueError) as va:
            self.robot = Robot('123', 'Military', 10, -3500)
        self.assertEqual(str(va.exception), "Price cannot be negative!")

    def test_upgrade(self):
        self.robot.hardware_upgrades = ["Head", "Arm"]
        result = self.robot.upgrade('Head', 150)
        self.assertEqual(result, "Robot 123 was not upgraded.")
        result = self.robot.upgrade('Leg', 350)
        self.assertEqual(result, 'Robot 123 was upgraded with Leg.')
        self.assertEqual(self.robot.hardware_upgrades, ["Head", "Arm", "Leg"])
        self.assertEqual(self.robot.price, 4025.0)

    def test_update(self):
        self.robot.software_updates = [1.0, 1.01]
        result = self.robot.update(0.9, 1)
        self.assertEqual(result, "Robot 123 was not updated.")
        result = self.robot.update(1.9, 11)
        self.assertEqual(result, "Robot 123 was not updated.")
        result = self.robot.update(1.9, 1)
        self.assertEqual(result, 'Robot 123 was updated to version 1.9.')
        self.assertEqual(self.robot.software_updates, [1.0, 1.01, 1.9])
        self.assertEqual(self.robot.available_capacity, 9)

    def test_if_robot2_greater_price_than_robot1(self):
        self.robot1 = Robot('123', 'Military', 10, 3500)
        self.robot2 = Robot('124', 'Military', 10, 4500)
        result = self.robot2 > self.robot1
        self.assertEqual(result, 'Robot with ID 124 is more expensive than Robot with ID 123.')

    def test_if_robot1_equal_price_than_robot2(self):
        self.robot1 = Robot('123', 'Military', 10, 3500)
        self.robot2 = Robot('124', 'Military', 10, 3500)
        result = self.robot2 > self.robot1
        self.assertEqual(result, 'Robot with ID 124 costs equal to Robot with ID 123.')

    def test_if_robot1_greater_price_than_robot2(self):
        self.robot1 = Robot('123', 'Military', 10, 4500)
        self.robot2 = Robot('124', 'Military', 10, 3500)
        result = self.robot2 > self.robot1
        self.assertEqual(result, 'Robot with ID 124 is cheaper than Robot with ID 123.')












