

from typing import Literal
from utils.pointable import Pointable
from .lake import Lake


class OrderedLake(Lake):
    def __init__(self, *objects: Pointable) -> None:
        super().__init__(*objects)
        self.X_order = list(objects)
        self.Y_order = list(objects)
        self.X_order.sort(key=lambda point: point.x())
        self.Y_order.sort(key=lambda point: point.y())

    def through_axe(self, axe: Literal["X", "Y"]):
        axe_order = self.__getattribute__(axe + "_order")
        n = len(axe_order)
        for i, point in enumerate(axe_order):
            if i == n-1: break
            yield point, axe_order[i+1]


    def through_X(self):
        for tup in self.through_axe("X"):
            yield tup

    def through_Y(self):
        for tup in self.through_axe("Y"):
            yield tup
        

    def add_to_me(self, object_creator):
        o = object_creator()
        self.add(o)
        self.X_order.append(o)
        self.Y_order.append(o)
        return o

