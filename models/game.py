from models.player import Player

class Game:

    def __init__(self, name, players):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def check_choice(self):
        for player in self.players:
            if player.choice == "rock" or player.choice == "paper" or player.choice == "scissors":
                return True
            return False

    def check_choice(self):
            if self.players[choice][0] == "rock" or self.players.choice[0] == "paper" or self.players.choice[0] == "scissors":
                if self.players.choice[1] == "rock" or self.players.choice[1] == "paper" or self.players.choice[1] == "scissors":
                    return True
                return False
            return False          

    def game_outcome(self):
        if self.check_choice() == True:
            if self.players[0].choice == "rock" and self.players[1].choice == "scissors":
                return "Player1 wins with rock"
            if self.players[0].choice == "paper" and self.players[1].choice == "rock":
                return "Player1 wins with paper"
            if self.players[0].choice == "scissors" and self.players[1].choice == "paper":
                return "Player1 wins with scissors"
            if self.players[0].choice == self.players[1].choice:
                return "It's a draw!"
            return f"Player2 wins with {self.players[1].choice}"
        return "Oops, invalid choice. Only use rock, paper or scissors. Try again."

