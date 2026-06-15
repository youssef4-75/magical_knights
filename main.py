import pygame as pg

from game.game_manager import GameManager

from objects import ControlPannel, Player

from screen.background import WithBackGround
from utils import Vector


# ------------------------- 1. creating the game ---------------------



win_size = (800, 600)
game = GameManager.init("Magical Knights", win_size)



# ------------------------- 2. Adding players ---------------------

control1 = ControlPannel(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
control2 = ControlPannel(pg.K_w, pg.K_s, pg.K_a, pg.K_d)
control3 = ControlPannel(pg.K_y, pg.K_h, pg.K_g, pg.K_j)
control4 = ControlPannel(pg.K_f, pg.K_v, pg.K_c, pg.K_b)

@game.add
def player(): return Player("me", "red", Vector.random(*win_size).to_tuple(), control1)
# displayer = Displayer(win, "grey", "red", pg.Rect(10, 10, 100, 20), value_provider = (lambda : game.addct.HP), max_provider = lambda :100)

@game.add
def player(): return Player("you", "blue", Vector.random(*win_size).to_tuple(), control2)

@game.add
def player(): return Player("you", "green", Vector.random(*win_size).to_tuple(), control3)

@game.add
def player(): return Player("you", "yellow", Vector.random(*win_size).to_tuple(), control4)


# ------------------------- 3. Adding displayers ---------------------

def value_provider(player: Player):
    return player.HP


r = []
for i in range(1, 5):
    r.append(
        pg.Rect(10, 30 * i, 100, 20)
    )

game.create_disp_for_players("grey", "red", *r, value_provider=value_provider)


# ------------------------- 4. The window's plugin ---------------------
bg = WithBackGround("assets/bg.png")
game.add_plugin(bg)
# ------------------------- -1. The game loop ---------------------
while game.running:
    for event in game.key_events():
        ...

    game.loop()