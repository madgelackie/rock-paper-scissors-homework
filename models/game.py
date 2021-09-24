# class Game:

#     def __init__(self, name):
#         self.name = name


def game_outcome(weapon1, weapon2):
    if weapon1 == "rock" and weapon2 == "scissors":
        return "weapon1 wins"
    if weapon1 == "paper" and weapon2 == "rock":
        return "weapon1 wins"
    if weapon1 == "scissors" and weapon2 == "paper":
        return "weapon1 wins"
    if weapon1 == weapon2:
        return "no one wins"
    return "weapon 2 wins"

