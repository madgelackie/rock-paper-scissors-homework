from flask import render_template
from app import app
from models.game import game_outcome
from models.player import *

@app.route('/')
def trial():
    return "ello worlds"

@app.route('/<weapon1>/<weapon2>')
def outcome(weapon1, weapon2):
    player1 = Player("player_uno", weapon1)
    player2 = Player("player_deux", weapon2)
    players = [player1, player2]
    game_outcome(weapon1, weapon2)
    # So now I need to get the output of game_outcome to be taken in by the index.html file to determine it's output
    return render_template("index.html", players=players)