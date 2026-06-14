


from objects import Player
from screen import Window
from utils import Singleton
from .drawer import Drawer


class PlayerDrawer(Drawer, Singleton):
    def draw(self, window: Window, player: Player):
        return window.draw(player.surf, player.rect)