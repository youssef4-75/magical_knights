import pygame as pg


from container.objects_container import ObjectsContainer
from services.force.repeller import Repeller
from services.translate.player_translater import PlayerTranslater
from objects import ControlPannel, Player

from services import PlayerDrawer
from utils import Vector
from screen import Window




control = ControlPannel(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)



repeller = Repeller()
drawer = PlayerDrawer()
translater = PlayerTranslater()

win = Window("Game", *(800, 600))

lake = ObjectsContainer(win)

@lake.add_to_me
def player(): return Player("me", "red", (300, 300), control)

# player = Player("me", "red")
# lake.add(player)


while win.running:
    win.fill((0, 0, 0))
    for event in win.events():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            repeller.repel(p, 30*Vector.up())
    
    for p in lake:
        drawer.draw(win, p)
        translater.translate(p)
    
    win.display()










