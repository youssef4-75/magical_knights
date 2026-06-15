

from typing import Callable
import pygame as pg

from objects.life_mixin import LifeMixin
from objects.motion_mixin import MotionMixin
from utils.vector import Vector




class ConsciousMixin:
    def __init__(self) -> None:
        self.__keys_actions: dict[list[int], list[Callable, int]]
        self.__console: dict[str, int]

    @staticmethod
    def start(self, console, keys_action: dict|None=None, **kwargs):
        if keys_action is None:
            keys_action = {}
        self.__keys_actions = keys_action
        for key, action in kwargs.items():
            self.__keys_actions[key] = action
        self.__console = console

    @property 
    def console(self):
        return self.__console

    def act(self, **context):
        keys_map = pg.key.get_pressed()
        for keys, (action, mana) in self.__keys_actions.items():
            casted = True
            for key in keys:
                if not keys_map[key]:
                    casted = False
            if casted:
                cani = self.to_life_mixin(mana)
                if cani: action(**context)
        
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

    def add_action(self, *keys: int, mana, action: Callable): 
        self.__keys_actions[keys] = [action, mana]

    def add_console(self, console: dict[str, int]=None, **kwargs):
        if console: 
            self.console.update(console)
        self.console.update(kwargs)

    @property 
    def actions(self):
        return self.__keys_actions
    
    def my_action(self, *keys, mana):
        def deco(function):
            self.add_action(*keys, mana=mana, action=function)
            return function
        return deco

    def to_motion_mixin(self, vector: Vector):
        assert isinstance(self, MotionMixin)
        self.move(vector)

    def to_life_mixin(self, price: int):
        assert isinstance(self, LifeMixin)
        return self.consume(price)