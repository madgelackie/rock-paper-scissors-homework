from flask import render_template
from app import app
from models.game import *
from models.player import *

@app.route('/welcome')
@app.route('/')
def welcome_page():
    return render_template("welcome.html", title = "Rules")

@app.route('/<weapon1>/<weapon2>')
@app.route('/<weapon1>/<weapon2>/')
def outcome(weapon1, weapon2):
    player1 = Player("player_uno", weapon1)
    player2 = Player("player_deux", weapon2)
    players = [player1, player2]
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(player2)
    rps.game_outcome()
    return render_template("index.html", players=players, rps=rps)