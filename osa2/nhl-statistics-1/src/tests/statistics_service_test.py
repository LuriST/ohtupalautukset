import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_ei_loydy_pelaajaa(self):
        player = self.stats.search("Messi")

        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_ei_loydy_pelaajia(self):
        players = self.stats.team("BOS")

        self.assertEqual(players, [])

    def test_top_palauttaa_parhaat_pelaajat(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_palauttaa_kaikki_jos_pyynto_on_suurempi(self):
        players = self.stats.top(10)

        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Gretzky")