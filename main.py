import pygame as pg


from container.objects_container import ObjectsContainer
from interaction_registry import InteractionsRegistry
from objects.game_object import GameObject
from services.force.repeller import Repeller
from services.translate.player_translater import PlayerTranslator
from objects import ControlPannel, Player

from services import PlayerDrawer
from utils import Vector
from screen import Window




control1 = ControlPannel(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
control2 = ControlPannel(pg.K_w, pg.K_s, pg.K_a, pg.K_d)



repeller = Repeller()
drawer = PlayerDrawer()
translater = PlayerTranslator()

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
            repeller.repel(player, 30*Vector.up())
    
    for p in lake:
        drawer.draw(win, p)
        translater.translate(p)


    lake.interaction()

    # for i in range(n):
    #     for j in range(i+1, n):
    #         o1: GameObject = lake[i]
    #         o2: GameObject = lake[j]
    #         if not o1.rect.colliderect(o2.rect): 
    #             continue
    #         InteractionsRegistry.map(o1.typeIdentifier(), o2.typeIdentifier())(o1, o2)
    
    win.display()








# from pygame import Rect


# r1, r2 = Rect(316, 286, 30, 30), Rect(320, 280, 30, 30)

# print(r1.colliderect(r2))