from project.toy_store import ToyStore

import unittest

class TestToyStore(unittest.TestCase):
    def test_add_toy(self):
        dict_toy_shelf = ToyStore.toy_shelf

        with self.assertRaises(ValueError) as er:
            dict_toy_shelf.add_toy("A", "kk")
        self.assertEqual("Shelf doesn't exist!", str(er.exception))

