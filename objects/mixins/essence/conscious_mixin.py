

from typing import Any, Callable
import pygame as pg

from .life_mixin import LifeMixin
from .motion_mixin import MotionMixin

from ....types_tools import Action
from ....utils import Vector




class ConsciousMixin:
    def start(self, console: dict|None = None, keys_action: dict|None=None, **kwargs):
        if keys_action is None:
            keys_action = {}
        setattr(self, "__keys_actions", keys_action)
        for key, action in kwargs.items():
            self.keys_actions[key] = action
        self.__console = console
        if console is None: 
            console = {
            "up": -1,
            "down": -1,
            "left": -1,
            "right": -1,
        }
        setattr(self, "__console", console)

    @property 
    def console(self):
        return getattr(self, "__console")
    
    @property
    def keys_actions(self):
        return getattr(self, "__keys_actions", {})

    def act(self, **context):
        keys_map = pg.key.get_pressed()
        for keys, (action, mana, cooldown, last_time_used) in self.keys_actions.items():
            if last_time_used[0]<cooldown: 
                last_time_used[0] += 1
                continue
            casted = True
            for key in keys:
                if not keys_map[key]:
                    casted = False
            if casted:
                cani = self.to_life_mixin(mana)
                if cani: 
                    last_time_used[0] = 0
                    action(**context)


        
        vector = Vector()
        if keys_map[self.console["up"]]:
            vector += Vector.up()
        if keys_map[self.console["down"]]:
            vector += Vector.down()
        if keys_map[self.console["left"]]:
            vector += Vector.left()
        if keys_map[self.console["right"]]:
            vector += Vector.right()

        self.to_motion_mixin(vector)

    def add_action(self, *keys: int, mana: int, cooldown: int, initial_delay: int, action: Action): 
        self.keys_actions[keys] = [action, mana, cooldown, [cooldown-initial_delay]]

    def add_actions(self, map: dict[tuple[tuple[int]|int, int, int, int], Action]):
        for (keys, mana, cooldown, initial_delay), action in map.items():
            if isinstance(keys, int): keys = (keys,)
            self.add_action(*keys, mana=mana, cooldown=cooldown, 
                    initial_delay=initial_delay, action=action)

    def add_console(self, console: dict[str, int]=None, **kwargs):
        if console: 
            self.console.update(console)
        self.console.update(kwargs)

    def my_action(self, *keys, mana, cooldown, initial_delay):
        def deco(function):
            self.add_action(*keys,
                mana=mana, cooldown=cooldown, initial_delay=initial_delay, 
                            action=function)
            return function
        return deco

    def to_motion_mixin(self, vector: Vector):
        assert isinstance(self, MotionMixin)
        self.move_in_direction(vector)

    def to_life_mixin(self, price: int):
        assert isinstance(self, LifeMixin)
        return self.consume(price)