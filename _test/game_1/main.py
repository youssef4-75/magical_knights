import pygame as pg

from ...game import GameManager



from .players import main as main_players
from .plugins import main as main_plugin



def main():
    # ------------------------- 1. creating the game ---------------------



    win_size = (800, 600)
    game = GameManager.init("Magical Knights", win_size)



    # ------------------------- 2. Adding players ---------------------
    main_players(game, win_size)

    # ------------------------- 3. The window's plugin ---------------------
    main_plugin(game)

    # ------------------------- -1. The game loop ---------------------
    while game.running:
        for event in game.key_events():
            ...

        game.loop()