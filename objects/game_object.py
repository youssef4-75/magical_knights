


from abc import ABC, abstractmethod

from objects.interaction_mixin import InteractionMixin
from utils.variables import MAX_MP


from .life_mixin import LifeMixin
from .motion_mixin import MotionMixin
from .shape_mixin import ShapeMixin


class GameObject(MotionMixin, ShapeMixin, LifeMixin, InteractionMixin, ABC):
    def __init__(self, left, top, width, height, color=None, speed=0, *, TTL=float("inf"), HP=100, MP=100, **kwargs) -> None:
        
        MotionMixin.start(self, left, top, width, height, speed)
        ShapeMixin.start(self, width, height, color)
        LifeMixin.start(self, TTL, HP, MP)
        InteractionMixin.start(self, **kwargs)
    
    @abstractmethod
    def typeIdentifier(self): ...

    @abstractmethod
    def draw(self, window):
        """this tells the drawer manager how this object is drawn in the window"""

    @abstractmethod
    def translate(self):
        """this tells the translator manager how this objects receive motions from the user input"""

    def advance(self):
        self.advance_rect()
        self.advance_surf()
        self.advance_life()