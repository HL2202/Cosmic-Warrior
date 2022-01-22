"""
This is the entry point to your game.

Launch the game by running `python3 launch_game.py`
"""

from game_engine import Engine
from gui import GUI
from player import Player

game = Engine('examples/basic_state_copy.txt', Player, GUI)

game.run_game()

#If the spaceship is too close to an asteroid it will not move and try to turn in another direction to get away from the asteroid as soon as possible