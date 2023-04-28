from project.movie import Movie

import unittest
# from unittest import TestCase, main


class TestMovie(unittest.TestCase):
    def test_init_with_valid_data(self):
        movie = Movie("K9", 1989, 5.5)
        self.assertEqual('K9', movie.name)
        self.assertEqual(1989, movie.year)
        self.assertEqual(5.5, movie.rating)
        self.assertEqual([], movie.actors)

    def test_movie_name_setter(self):
        with self.assertRaises(ValueError) as er:
            Movie("", 1989, 5.5)
        self.assertEqual("Name cannot be an empty string!", str(er.exception))

    def test_movie_year_setter(self):
        with self.assertRaises(ValueError) as er:
            Movie("K9", 1886, 5.5)
        self.assertEqual("Year is not valid!", str(er.exception))

    def test_add_actor_not_in_list(self):
        movie = Movie("K9", 1989, 5.5)
        movie.actors = ["ivan"]
        movie.add_actor('gosho')
        self.assertEqual(["ivan", "gosho"], movie.actors)

    def test_add_actor_is_in_list(self):
        movie = Movie("K9", 1989, 5.5)
        movie.actors = ["ivan", "gosho"]
        self.assertEqual("gosho is already added in the list of actors!", movie.add_actor('gosho'))

    def test_gt_magic_method(self):
        movie1 = Movie("K9", 1989, 5.5)
        movie2 = Movie("Rock", 1988, 6.0)
        self.assertEqual('"Rock" is better than "K9"', movie1 > movie2)
        self.assertEqual('"Rock" is better than "K9"', movie2 > movie1)
        self.assertEqual('"Rock" is better than "K9"', movie1 < movie2)
        self.assertEqual('"Rock" is better than "K9"', movie2 < movie1)

    def test_rept_magic_method(self):
        movie = Movie("K9", 1989, 5.5)
        movie.actors = ["ivan", "gosho"]
        expected = f"Name: K9\n" \
               f"Year of Release: 1989\n" \
               f"Rating: 5.50\n" \
               f"Cast: ivan, gosho"
        actual = repr(movie)
        self.assertEqual(expected, actual)

# if __name__ == '__main__':
#     main()
