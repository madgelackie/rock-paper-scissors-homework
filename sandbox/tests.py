import unittest
from models.game import *
from models.player import *

import unittest
from src.task import Task

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