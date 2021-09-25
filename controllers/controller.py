from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/')
def wecome_page():
    return "Welcome to ROCK PAPER SCISSORS. Enter your weapon of choice in the browser bar above"

@app.route('/<weapon1>/<weapon2>')
def outcome(weapon1, weapon2):
    player1 = Player("player_uno", weapon1)
    player2 = Player("player_deux", weapon2)
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(player2)
    rps.game_outcome()
    # So now I need to get the output of game_outcome to be taken in by the index.html file to determine it's output
    return render_template("index.html", rps=rps)