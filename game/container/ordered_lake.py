

from typing import Literal
from utils.pointable import Pointable
from .lake import Lake
from icecream import ic

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


    def add(self, *elements: Pointable):
        for element in elements:
            self.objects.append(element)
            self.X_order.append(element)
            self.Y_order.append(element)

    def through_X(self):
        for tup in self.through_axe("X"):
            yield tup

    def through_Y(self):
        for tup in self.through_axe("Y"):
            yield tup
        

    def add_to_me(self, object_creator):
        o = object_creator()
        self.add(o)
        return o

    def remove(self, object):
        # ic(self.objects, "\n", self.X_order, "\n", self.Y_order, "\n", object)
        self.objects.remove(object)
        self.X_order.remove(object)
        self.Y_order.remove(object)

    def update(self):
        self.X_order.sort(key=lambda point: point.x())
        self.Y_order.sort(key=lambda point: point.y())