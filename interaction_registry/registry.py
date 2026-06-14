from utils import PLAYER
from objects import Player



class InteractionsRegistry:
    registry = {}

    def __init__(self, map) -> None:
        pass

    @staticmethod
    def map(class1, class2):
        return InteractionsRegistry.registry.get((class1, class2), lambda *__, **_:None)
    

    @staticmethod
    def add_to_me(class1, class2):
        def deco(function):
            InteractionsRegistry.registry[(class1, class2)] = function
        return deco


