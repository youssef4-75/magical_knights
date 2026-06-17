
from typing import Callable
from .item import Item


def reorder(a, b):
    return min(a, b), max(a, b)

def reclassify[A, B](obj1: A|B, obj2: A|B, *, _1st_class: type, _2nd_class: type) -> tuple[A, B]:
    if isinstance(obj1, _1st_class):
        return obj1, obj2 
    if isinstance(obj1, _2nd_class):
        return obj2, obj1
    raise Exception("both objects are of the same class, cannot reclassify")


def add_to_registry(registry, item: Item):
    class1, class2, function = item.extract()
    registry[reorder(class1, class2)] = function

def register(class1, class2) -> Callable:
    def deco(function) -> Item:
        return Item(class1, class2, function)
    return deco