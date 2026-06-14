import pygame as pg


from container import ObjectsContainer
from services import ServicesManager, Repeller, PlayerTranslator, PlayerDrawer
from objects import ControlPannel, Player

from utils import Vector
from screen import Window
from utils.displayer import Displayer




control1 = ControlPannel(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
control2 = ControlPannel(pg.K_w, pg.K_s, pg.K_a, pg.K_d)
control3 = ControlPannel(pg.K_y, pg.K_h, pg.K_g, pg.K_j)
control4 = ControlPannel(pg.K_f, pg.K_v, pg.K_c, pg.K_b)



services_manager = ServicesManager(
    PlayerDrawer(),
    Repeller(),
    PlayerTranslator(),
)

win_size =  (800, 600)
win = Window("Game", *win_size)

lake = ObjectsContainer()

@lake.add_to_me
def player(): return Player("me", "red", Vector.random(*win_size).to_tuple(), control1)
# displayer = Displayer(win, "grey", "red", pg.Rect(10, 10, 100, 20), value_provider = (lambda : lake[0].interact.HP), max_provider = lambda :100)

@lake.add_to_me
def player(): return Player("you", "blue", Vector.random(*win_size).to_tuple(), control2)

@lake.add_to_me
def player(): return Player("you", "green", Vector.random(*win_size).to_tuple(), control3)

@lake.add_to_me
def player(): return Player("you", "yellow", Vector.random(*win_size).to_tuple(), control4)

# player = Player("me", "red")
# lake.add(player)



while win.running:
    for event in win.events():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            ...
    
    for p in lake:
        services_manager.translate(p)
        services_manager.draw(win, p)

    lake.interaction()
    lake.garbage_collect()
    win.display()
    win.fill((0, 0, 0))










# from pygame import Rect


# r1, r2 = Rect(316, 286, 30, 30), Rect(320, 280, 30, 30)

# print(r1.colliderect(r2))