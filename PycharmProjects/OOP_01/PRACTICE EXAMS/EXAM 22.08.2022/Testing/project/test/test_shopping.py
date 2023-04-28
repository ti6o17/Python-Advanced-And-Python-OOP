import unittest

from project.shopping_cart import ShoppingCart


class TestShoppingCard(unittest.TestCase):
    def setUp(self):
        self.shopping_card = ShoppingCart('Tihomir', 1000)

    def test_init(self):
        self.assertEqual(self.shopping_card.shop_name, 'Tihomir')
        self.assertEqual(self.shopping_card.budget, 1000)
        self.assertEqual(self.shopping_card.products, {})

    def test_name_raises_exception1(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_card = ShoppingCart('tihomir', 1000)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_raises_exception2(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_card = ShoppingCart('8ihomir', 1000)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_raises(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_card.add_to_cart('Banica', 100.1)
        self.assertEqual(str(ex.exception), "Product Banica cost too much!")

    def test_add_to_cart_valid(self):
        result = self.shopping_card.add_to_cart('Banica', 3.4)
        self.assertEqual(self.shopping_card.products, {'Banica': 3.4})
        self.assertEqual(result, "Banica product was successfully added to the cart!")
        result = self.shopping_card.add_to_cart('Boza', 3.8)
        self.assertEqual(self.shopping_card.products, {'Banica': 3.4, 'Boza': 3.8})
        self.assertEqual(result, "Boza product was successfully added to the cart!")

    def test_remove_from_cart_raises(self):
        self.shopping_card.add_to_cart('Boza', 3.8)
        with self.assertRaises(ValueError) as ex:
            self.shopping_card.remove_from_cart('Banica')
        self.assertEqual(str(ex.exception), "No product with name Banica in the cart!")

    def test_remove_from_cart_valid(self):
        self.shopping_card.products = {'Banica': 3.4, 'Boza': 3.8}
        result = self.shopping_card.remove_from_cart('Banica')
        self.assertEqual(self.shopping_card.products, {'Boza': 3.8})
        self.assertEqual(result, "Product Banica was successfully removed from the cart!")

    def test__add__method(self):
        shopping_card1 = ShoppingCart('Tihomir', 2000)
        shopping_card1.products = {'Banica': 3.4}
        shopping_card2 = ShoppingCart('Stanislava', 1000)
        shopping_card2.products = {'Boza': 3.8}
        result = shopping_card1.__add__(shopping_card2)
        self.assertEqual(result.shop_name, 'TihomirStanislava')
        self.assertEqual(result.budget, 3000)
        self.assertEqual(result.products, {'Banica': 3.4, 'Boza': 3.8})


    def test_buy_products_raises(self):
        self.shopping_card.products = {'Banica': 501, 'Boza': 500}
        with self.assertRaises(ValueError) as ex:
            self.shopping_card.buy_products()
        self.assertEqual(str(ex.exception), "Not enough money to buy the products! Over budget with 1.00lv!")

    def test_buy_products_valid(self):
        self.shopping_card.products = {'Banica': 3.4, 'Boza': 3.8}
        result = self.shopping_card.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 7.20lv.')


if __name__ == '__main__':
    unittest.main()