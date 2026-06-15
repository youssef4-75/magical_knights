from objects import GameObject
from utils import Vector, REPULSE



class InteractionsRegistry:
    registry = {}

    def __init__(self, map) -> None:
        pass

    @staticmethod
    def map(class1, class2):
        if class2 < class1: 
            class1, class2 = class2, class1 
        return InteractionsRegistry.registry.get((class1, class2), lambda *__, **_:None)
    

    @staticmethod
    def add_to_me(class1, class2):
        def deco(function):
            InteractionsRegistry.registry[
                min(class1, class2), max(class1, class2)
            ] = function
        return deco

    @staticmethod
    def default(obj1: GameObject, obj2: GameObject):
        vector12 = Vector(*obj1.rect.center) - Vector(*obj2.rect.center)
        r = vector12.magnitude()
        if r==0:
            return 
        direction = (REPULSE/r) * vector12.normalize()
        obj1.set_accel(direction)
        obj2.set_accel(-direction)


