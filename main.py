import pygame as pg


from container import ObjectsContainer
from services import ServicesManager, Repeller, PlayerTranslator, PlayerDrawer
from objects import ControlPannel, Player

from utils import Vector
from screen import Window




control1 = ControlPannel(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
control2 = ControlPannel(pg.K_w, pg.K_s, pg.K_a, pg.K_d)


services_manager = ServicesManager(
    PlayerDrawer(),
    Repeller(),
    PlayerTranslator(),
)

win = Window("Game", *(800, 600))

lake = ObjectsContainer()

@lake.add_to_me
def player(): return Player("me", "red", (30, 30), control1)

@lake.add_to_me
def player(): return Player("you", "blue", (300, 300), control2)

# player = Player("me", "red")
# lake.add(player)
n = len(lake)


while win.running:
    win.fill((0, 0, 0))
    for event in win.events():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            sm.repel(player, 30*Vector.up())
    
    for p in lake:
        sm.draw(win, p)
        sm.translate(p)


    lake.interaction()

    win.display()








# from pygame import Rect


# r1, r2 = Rect(316, 286, 30, 30), Rect(320, 280, 30, 30)

# print(r1.colliderect(r2))