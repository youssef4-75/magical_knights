


from player import Player
from window import Window
from .drawer import Drawer


class PlayerDrawer(Drawer):
    def draw(self, window: Window, player: Player):
        return window.draw(player.surf, player.rect)