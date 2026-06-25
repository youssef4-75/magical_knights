
from ...plugins import WithBackGround, WithPDisplayer, WithNoOverlaps
from ...utils import from_root



def main(game):
    disp = WithPDisplayer()
    bg = WithBackGround(from_root("assets/bg1.png"))
    no = WithNoOverlaps()
    game.add_plugin(bg, disp, no)