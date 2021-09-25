import unittest

from game import Game
from player import Player


class TestTask(unittest.TestCase):

    def setUp(self):
        self.game = Game("RPS", [])
        self.playerA = Player("Jim", "rock")
        self.playerB = Player("Gemma", "paper")
        self.playerC = Player("Tim", "rock")

    def test_game_has_name(self):
        self.assertEqual("RPS", self.game.name)


    # def test_task_has_description(self):
    #     self.assertEqual("Wash Dishes", self.task.description)


    # def test_task_has_duration(self):
    #     self.assertEqual(10, self.task.duration)