


from ..objects import GameObject
from ..utils import K_FRICTION
from ..game import Plugin


class WithFriction(Plugin):

    def __init__(self, friction=K_FRICTION):
        self.__friction = friction 
    
    def activate(self, game):
        ...

    def init(self, game):
        ...

    def behaviour(self, gobj: GameObject):
        gobj.accel -= self.__friction * gobj.vel 

    def interaction(self, gobj1, gobj2):
        ...