import pygame as pg


from ..screen import Window


class WindowMixin: 
    def __init__(self, window: Window, *__, **_) -> None:
        super().__init__(*__, **_)
        self.window: Window = window 

    # window
    def draw(self, surface: pg.Surface, rect: pg.Rect):
        return self.window.draw(surface, rect)

    @property
    def screen_size(self):
        return self.window.size()