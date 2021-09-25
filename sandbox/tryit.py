# class Player:
#     def __init__(self, input_name, input_url):
#         self.name = input_name
#         self.choice = input_url
        
# # ["rock", "paper", "scissors"]        

# player1 = Player("James", "bloop")

# print(player1.name)

# print(player1.choice)

# class Game:

#     def __init__(self, players):
#         self.players = []


#     def game_outcome(self, weapon1, weapon2):
#         if weapon1 == "rock" and weapon2 == "scissors":
#             return "Player1 wins with rock"
#         if weapon1 == "paper" and weapon2 == "rock":
#             return "Player1 wins with paper"
#         if weapon1 == "scissors" and weapon2 == "paper":
#             return "Player1 wins with scissors"
#         if weapon1 == weapon2:
#             return
#         return f"Player2 wins with {weapon2}"

# rps = Game([])
# rps.players.append("player1")
# rps.players.append("player2")


# winner = rps.game_outcome("rock", "rock")
# print (winner)
class Player:

    def __init__(self, input_name, input_choice):
        self.name = input_name
        self.choice = input_choice

player1 = Player("jim", "paper")
player2 = Player("sharon", "scisors")


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
        return "Invalid choice, only use rock, paper or scissors! Try again."

rps = Game("RPS", [])
rps.add_player(player1)
rps.add_player(player2) 
player_list = len(rps.players)
print (player_list)
print (rps.check_choice())
print (rps.game_outcome())

