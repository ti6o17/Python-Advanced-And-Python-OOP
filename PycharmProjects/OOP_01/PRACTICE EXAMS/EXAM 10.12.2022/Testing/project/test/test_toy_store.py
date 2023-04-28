from project.toy_store import ToyStore

import unittest


class TestToyStoreClass(unittest.TestCase):
    def test_correct_init(self):
        toy_store = ToyStore()
        self.assertTrue(toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_correct_add_toy(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy("A", "Bibi")
        self.assertEqual(result, "Toy:Bibi placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "Bibi",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_if_shelf_doesnt_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "Babi")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_if_toy_exist(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Babi")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Babi")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_if_shelf_taken(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Babi")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Babik")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_remove_toy_successful(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Babi")
        result = self.toy_store.remove_toy("A", "Babi")
        self.assertEqual(result, "Remove toy:Babi successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_if_toy_not_in_shelf(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Babi")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_if_toy_in_shelf_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("K", "Babio")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")


if __name__ == '__main__':
    unittest.main()