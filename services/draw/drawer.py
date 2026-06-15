
from screen import Window
from objects import GameObject


class Drawer:
    def draw(self, window: Window, obj: GameObject):
        return obj.draw(window)