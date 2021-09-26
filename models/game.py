
from models.player import Player


class Game:

    def __init__(self, name, players):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def player_choices_list(self):
        player_choices = []
        for player in self.players:
            player_choices.append(player.choice)
        return (player_choices)

    def check_choice(self):
            if self.players[0].choice == "rock" or self.players[0].choice == "paper" or self.players[0].choice == "scissors":
                if self.players[1].choice == "rock" or self.players[1].choice == "paper" or self.players[1].choice == "scissors":
                    return True
            return False 

    def game_outcome(self):
        if self.check_choice() == True:
            if self.players[0].choice == "rock" and self.players[1].choice == "scissors":
                return "Player 1 wins with rock"
            if self.players[0].choice == "paper" and self.players[1].choice == "rock":
                return "Player 1 wins with paper"
            if self.players[0].choice == "scissors" and self.players[1].choice == "paper":
                return "Player 1 wins with scissors"
            if self.players[0].choice == self.players[1].choice:
                return "It's a draw!"
            return f"Player 2 wins with {self.players[1].choice}"
        return "Oops, invalid choice. Only use rock, paper or scissors. Try again."

    def game2_outcome(self):
            if self.check_choice() == True:
                if self.players[0].choice == "rock" and self.players[1].choice == "scissors":
                    return "You win with rock"
                if self.players[0].choice == "paper" and self.players[1].choice == "rock":
                    return "You win with paper"
                if self.players[0].choice == "scissors" and self.players[1].choice == "paper":
                    return "You win with scissors"
                if self.players[0].choice == self.players[1].choice:
                    return "It's a draw!"
                return f"Your imaginary friend wins with {self.players[1].choice}"
            return "Oops, invalid choice. Only use rock, paper or scissors. Try again."
