import unittest

from project.bookstore import Bookstore


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(100)

    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 100)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_book_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = -1
        self.assertEqual(str(ex.exception), "Books limit of -1 is not valid")

    def test_book_limit_valid(self):
        self.bookstore.books_limit = 1
        self.assertEqual(self.bookstore.books_limit, 1)

    def test_receive_book_raises(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 30, 'b': 30, 'c': 30}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('d', 101)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 30, 'b': 30, 'c': 30}
        result = self.bookstore.receive_book('d', 9)
        self.assertEqual(result, "9 copies of d are available in the bookstore.")

    def test_sell_book_raises1(self):
        self.bookstore.availability_in_store_by_book_titles = {'a': 30, 'b': 30, 'c': 30}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('d', 1)
        self.assertEqual(str(ex.exception), "Book d doesn't exist!")

    def test_sell_book_raises2(self):
        self.bookstore.availability_in_store_by_book_titles = {'Title': 30, 'b': 30, 'c': 30}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title', 31)
        self.assertEqual(str(ex.exception), "Title has not enough copies to sell. Left: 30")

    def test_sell_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles = {'Title': 30, 'b': 30, 'c': 30}
        result = self.bookstore.sell_book('Title', 5)
        self.assertEqual(result, "Sold 5 copies of Title")

    def test_final_total_sold_books_str(self):
        self.bookstore.availability_in_store_by_book_titles = {'Title1': 30, 'Title2': 30}
        self.bookstore.sell_book('Title1', 5)
        self.bookstore.sell_book('Title2', 10)
        self.assertEqual(str(self.bookstore), "Total sold books: 15\n"
                                                'Current availability: 45\n'
                                                " - Title1: 25 copies\n"
                                                " - Title2: 20 copies")






if __name__ == '__main__':
    unittest.main()
