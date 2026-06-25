
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
        self.add_default_interactions_lakeM(*self.interactions)

        
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
        for gobj in self.lake:
            self.draw(gobj.surf, gobj.rect)
            if gobj.is_conscious():
                for behaviour in self.behaviours:
                    behaviour(gobj)
                gobj.act(acter=gobj, game=self)

        self.lake.interaction()
        self.lake.garbage_collect(self)
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

