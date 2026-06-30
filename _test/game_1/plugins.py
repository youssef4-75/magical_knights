

from ...plugins import WithBackGround, WithPDisplayer, WithNoOverlaps, WithFriction
from ...utils import from_root



def main(game):
    disp = WithPDisplayer()
    bg = WithBackGround(from_root("assets/bg1.png"))
    no = WithNoOverlaps()
    fric = WithFriction(0.02)
    game.add_plugin(bg, disp, no, fric)