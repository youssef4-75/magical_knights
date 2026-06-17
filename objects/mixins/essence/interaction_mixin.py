
from typing import Any
from pygame import Rect

from utils import Mixin


class InteractionMixin(Mixin):
    def __init__(self) -> None:
        self.__data: dict; self.__aura: int
        self.__detrect: Rect

    def start(self, motion_rect: Rect, aura: int=0, **kwargs):
        self.__detrect = Rect(0, 0, motion_rect.width + 2*aura, motion_rect.height + 2*aura, )
        self.__detected = []
        self.__aura = aura
        self.__data = kwargs

    @property
    def aura(self):
        return self.__aura
    
    def detecting(self, other_rect: Rect):
        if self.__detrect.colliderect(other_rect):
            self.__detected.append(other_rect)
    
    def advance_interaction(self):
        ...

    def near(self):
        for obj in self.__detected:
            yield obj 


    def get_IV(self, name: str):
        return self.__data.get(name)

    def set_IV(self, name: str, value: Any):
        self.__data[name] = value

    def add_IV(self, name: str, value: Any):
        if not name in self.__data:
            return
        self.__data[name] += value
