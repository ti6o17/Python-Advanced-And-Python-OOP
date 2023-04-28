import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer('Tisho', 44, 100)

    def test_init(self):
        self.assertEqual(self.tennis_player.name, 'Tisho')
        self.assertEqual(self.tennis_player.age, 44)
        self.assertEqual(self.tennis_player.points, 100)
        self.assertEqual(self.tennis_player.wins, [])

    def test_init_name_raises(self):
        with self.assertRaises(ValueError) as va:
            self.tennis_player = TennisPlayer('Ti', 44, 100)
        self.assertEqual(str(va.exception), "Name should be more than 2 symbols!")

    def test_init_age_raises(self):
        with self.assertRaises(ValueError) as va:
            self.tennis_player = TennisPlayer('Tisho', 17, 100)
        self.assertEqual(str(va.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        self.tennis_player.add_new_win("Varna")
        self.assertEqual(self.tennis_player.wins, ["Varna"])
        result = self.tennis_player.add_new_win("Varna")
        self.assertEqual(result, "Varna has been already added to the list of wins!")

    def test_lessthan(self):
        self.tennis_player1 = TennisPlayer('Tisho', 44, 100)
        self.tennis_player2 = TennisPlayer('Stasi', 40, 75)

        result = self.tennis_player1 < self.tennis_player2
        self.assertEqual(result, 'Tisho is a better player than Stasi')

        self.tennis_player1 = TennisPlayer('Tisho', 44, 75)
        self.tennis_player2 = TennisPlayer('Stasi', 40, 100)

        result = self.tennis_player1 < self.tennis_player2
        self.assertEqual(result, 'Stasi is a top seeded player and he/she is better than Tisho')

    def test_str(self):
        self.tennis_player = TennisPlayer('Tisho', 44, 100)
        self.tennis_player.wins = ['Varna']
        result = str(self.tennis_player)
        self.assertEqual(result, "Tennis Player: Tisho\nAge: 44\nPoints: 100.0\nTournaments won: Varna")

        self.tennis_player = TennisPlayer('Tisho', 44, 100)
        self.tennis_player.wins = ['Varna', 'Sofia']
        result = str(self.tennis_player)
        self.assertEqual(result, "Tennis Player: Tisho\nAge: 44\nPoints: 100.0\nTournaments won: Varna, Sofia")

    if __name__ == '__main__':
        unittest.main()
