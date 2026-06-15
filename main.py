import pygame as pg

from animation.animation import Animation
from game.game_manager import GameManager

from objects import Player

from objects import consolify
from screen.background import WithBackGround
from utils import Vector
from utils.variables import PLAYER_SIZE


# ------------------------- 1. creating the game ---------------------



win_size = (800, 600)
game = GameManager.init("Magical Knights", win_size)



# ------------------------- 2. Adding players ---------------------

control1 = consolify(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
control2 = consolify(pg.K_w, pg.K_s, pg.K_a, pg.K_d)
control3 = consolify(pg.K_y, pg.K_h, pg.K_g, pg.K_j)
control4 = consolify(pg.K_f, pg.K_v, pg.K_c, pg.K_b)

animation = Animation.from_directory("./assets/anim_set01/0x1", PLAYER_SIZE)

@game.add
def player(): 
    p = Player("me", "red", Vector.random(*win_size).to_tuple(), control1)
    p.attach_animation(animation)
    
    return p

@game.add
def player(): 
    p = Player("you", "blue", Vector.random(*win_size).to_tuple(), control2)
    @p.my_action(pg.K_p, mana=10)
    def jump(player: Player, *a, **k):
        player.set_accel(4*Vector.up())
    # p.add_action(pg.K_p, action=jump)
    return p

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