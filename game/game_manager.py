
import pygame as pg

from container.objects_container import ObjectsContainer
from objects.conscious_mixin import ConsciousMixin
from screen import Window
from utils.displayer import PlayerDisplayer
from utils.displayer_abc import DisplayerABC


class GameManager:
    def __init__(self, win: Window, 
            lake: ObjectsContainer) -> None:
        self.window = win
        self.lake = lake
        self.displayers: list[DisplayerABC] = []
        
    @classmethod
    def init(cls, name: str, win_size: tuple[int, int]):
        return cls(
            Window(name, *win_size),
            ObjectsContainer()
        )

    def add(self, object_creator):
        return self.lake.add_to_me(object_creator)

    def create_disp_for_players(self, bg_color, color, *rects, value_provider, maximum_provider=None):
        
        for i, obj in enumerate(self.lake):
            if i>=len(rects) and i!=0: rect = rects[-1]
            elif len(rects) == 0: raise Exception("no rects provided, minimum one rectangle is required")
            else: 
                rect = rects[i]
            displayer = PlayerDisplayer(
                self.window, bg_color, color, rect, 
                observable_obj=obj, 
                max_provider=maximum_provider, 
                value_provider=value_provider
                    )
            self.displayers.append(displayer)

    def add_displayer(self, displayer: DisplayerABC):
        self.displayers.append(displayer)

    def loop(self):
        self.window.activate_plugins()

        for p in self.lake:
            p.draw(self.window)
            if isinstance(p, ConsciousMixin):
                # print(p.actions)
                p.act(player=p, game=self)
        
        for displayer in self.displayers:
            displayer.display()

        self.lake.interaction()
        self.lake.garbage_collect()

        self.window.display()
        self.window.fill((0, 0, 0))



    @property
    def running(self):
        return self.window.running 
    
    def key_events(self):
        for event in self.window.events():
            if event.type == pg.KEYDOWN:
                yield event

    def add_plugin(self, *plugins):
        return self.window.add_plugin(*plugins)