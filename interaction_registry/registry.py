from .interactions_dictionary import registry
from ..objects import GameObject
from ..utils import Vector, REPULSE, get_interaction_normal



class InteractionsRegistryManager:
    registry = registry

    @staticmethod
    def map(class1, class2):
        if class2 < class1: 
            class1, class2 = class2, class1 
        return InteractionsRegistryManager.registry.get((class1, class2), lambda *__, **_:None)
    

    @staticmethod
    def add_to_me(class1, class2):
        def deco(function):
            InteractionsRegistryManager.registry[
                min(class1, class2), max(class1, class2)
            ] = function
        return deco

    @staticmethod
    def default(obj1: GameObject, obj2: GameObject):
        vector12 = Vector(*obj1.rect.center) - Vector(*obj2.rect.center)
        r = vector12.magnitude()
        # normal = get_interaction_normal(obj1.rect, obj2.rect)
        if r==0:
            return 
        direction = (REPULSE/r) * vector12.normalize() # normal 
        obj1.add_accel(direction)
        obj2.add_accel(-direction)


