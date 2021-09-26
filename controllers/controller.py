from flask import render_template
from app import app
import random
from models.game import *
from models.player import *

@app.route('/welcome')
@app.route('/')
def welcome_page():
    return render_template("welcome.html", title = "Welcome")

@app.route('/welcome/<weapon1>/<weapon2>')
@app.route('/welcome<weapon1>/<weapon2>/')
def outcome(weapon1, weapon2):
    player1 = Player("player_uno", weapon1)
    player2 = Player("player_deux", weapon2)
    players = [player1, player2]
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(player2)
    rps.game_outcome()
    return render_template("index.html", title="RPS", players=players, rps=rps)

@app.route('/computer')
# @app.route('/computer/')
def computer_match_set_up():
    return render_template("computer.html", title="Play Computer")    

@app.route('/computer/<weapon3>')
@app.route('/computer/<weapon3>/')
def computer_outcome(weapon3):
    player1 = Player("player_3", weapon3 )
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    player2 = Player("computer", choice)
    players = [player1, player2]
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(player2)
    rps.game2_outcome()
    return render_template("vscomputer.html", title="vs Computer", players=players, rps=rps)    

