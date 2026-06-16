
import pygame as pg

from .mixins import (
    LakeMixin, 
    PluginMixin, 
    WindowMixin
)


from .screen import Window


class GameManager(WindowMixin, LakeMixin, PluginMixin):
    def __init__(self, win: Window) -> None:
        super().__init__(win)

        
    @classmethod
    def init(cls, name: str, win_size: tuple[int, int]):
        return cls(
            Window(name, *win_size)
        )

    @property
    def name(self): 
        return self.window.title

    def loop(self):

        self.activate_plugins()
        for p in self.lake:
            p.draw(self.window)
            if p.is_conscious():
                # print(p.actions)
                p.act(player=p, game=self)

        self.lake.interaction()
        self.lake.garbage_collect()
        self.window.display()
        self.window.fill((0, 0, 0))

    # game
    @property
    def running(self):
        return self.window.running 
    
    # game
    def key_events(self):
        for event in self.window.events():
            if event.type == pg.KEYDOWN:
                yield event
