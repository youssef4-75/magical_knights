


from abc import ABC, abstractmethod

from .mixins import (
    ConsciousMixin, InteractionMixin, 
    LifeMixin, MotionMixin, ShapeMixin
)


class GameObject(MotionMixin, ShapeMixin, LifeMixin, InteractionMixin, ABC):
    def __init__(self, left, top, width, height, 
            color=None, speed=0, *, 
            TTL=float("inf"), HP=100, 
            MP=100, vel=None, accel=None,
            **kwargs) -> None:

        MotionMixin.start(self, left, top, 
                        width, height, 
                        speed, vel, accel)
        ShapeMixin.start(self, width, height, color)
        LifeMixin.start(self, TTL, HP, MP)
        InteractionMixin.start(self, **kwargs)
    
    @abstractmethod
    def typeIdentifier(self): ...

    def advance(self):
        self.advance_rect()
        self.advance_surf()
        self.advance_life()
    
    def is_conscious(self):
        return isinstance(self, ConsciousMixin)