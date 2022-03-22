import unittest
from statistics import Statistics
from player import Player


import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_works_when_player_in_players(self):
        searched = self.statistics.search("Lemieux")

        self.assertEqual(self.statistics.search("Lemieux"), searched)

    def test_search_works_when_player_not_in_players(self):
        self.assertIsNone(self.statistics.search("Jagr"))
    
    def test_search_players_of_team_works(self):
        searched = self.statistics.search("Yzerman")

        self.assertEqual(self.statistics.team("DET"), [searched])

    def test_top_scorers_works(self):
        searched = self.statistics.search("Gretzky")

        self.assertEqual(str(self.statistics.top_scorers(1)[0]), str(searched))