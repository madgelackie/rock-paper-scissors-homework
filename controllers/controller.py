from flask import render_template, request
import random
from app import app
from models.game import *
from models.player import *

@app.route("/")
def welcome_page():
    return render_template("index.html", title = "Welcome")

@app.route('/<weapon1>/<weapon2>/')
@app.route('/<weapon1>/<weapon2>')
def outcome(weapon1, weapon2):
    player1 = Player("player_uno", weapon1)
    player2 = Player("player_deux", weapon2)
    players = [player1, player2]
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(player2)
    rps.game_outcome()
    return render_template("outcome.html", players=players, rps=rps)

@app.route('/play')
def play():
    return render_template("play.html", title="vs Computer")

@app.route('/play', methods=['POST'])
def play_against_computer():
    weapon = request.form["player_choice"]
    player1 = Player("player_a", weapon)
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    computer = Player("player_b", computer_choice)
    players = [player1, computer]
    rps = Game("RPS", [])
    rps.add_player(player1)
    rps.add_player(computer)
    rps.game2_outcome()
    return render_template("play_outcome.html", title="outcome", players=players, rps=rps)
