import unittest

from models.game import Game
from models.player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game("RPS", [])
        self.playerA = Player("Jim", "rock")
        self.playerB = Player("Gemma", "paper")
        self.playerC = Player("Tim", "bloop")
        self.playerD = Player("Marion", "paper")

    def test_game_has_name(self):
        self.assertEqual("RPS", self.game1.name)

    def test_game_has_empty_player_list(self):
        self.assertEqual(0, len(self.game1.players))

    def test_can_add_player(self):
        self.game1.add_player(self.playerA)
        self.assertEqual(1, len(self.game1.players) )

    def test_players_in_game_made_valid_choice(self):
        self.game1.add_player(self.playerA)
        self.game1.add_player(self.playerB)
        self.assertEqual(True, self.game1.check_choice())

    def test_player1_in_game_made_invalid_choice(self):
        self.game1.add_player(self.playerC)
        self.game1.add_player(self.playerA)
        self.assertEqual(False, self.game1.check_choice())
        
    def test_player2_in_game_made_invalid_choice(self):   
        self.game1.add_player(self.playerA)
        self.game1.add_player(self.playerC)
        self.assertEqual(False, self.game1.check_choice())
    
    def test_game_outcome_if_invalid_choice(self):
        self.game1.add_player(self.playerA)
        self.game1.add_player(self.playerC)
        self.assertEqual("Oops, invalid choice. Only use rock, paper or scissors. Try again.", self.game1.game_outcome())
    
    def test_game_outcome_runs_if_valid_choices(self):
        self.game1.add_player(self.playerA)
        self.game1.add_player(self.playerB)
        self.assertEqual("Player2 wins with paper", self.game1.game_outcome())

    def test_draw_outcome(self):
        self.game1.add_player(self.playerB)
        self.game1.add_player(self.playerD)
        self.assertEqual("It's a draw!", self.game1.game_outcome())



    