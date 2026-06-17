import pygame as pg

from ....utils import Animation, AnimationSet, Mixin, FRAME_SPEED



class ShapeMixin(Mixin):
    def __init__(self, ):
        self.__surf: pg.Surface|Animation|AnimationSet; 
        self.__animation_active: bool
        self.__color: str|tuple|pg.Color|None

    def start(self, width, height, color):
        self.__surf = pg.Surface((width, height))
        self.__color = color
        if color is not None: 
            self.__surf.fill(color)
        self.__animation_active = False

    @property
    def surf(self):
        if self.__animation_active:
            return self.__surf.generate()
        return self.__surf
    
    @property
    def color(self):
        return self.__color
    
    def advance_surf(self):
        if not self.__animation_active:
            return

    def attach_animation(self, animation: Animation|AnimationSet, frame_speed=FRAME_SPEED):
        if isinstance(animation, Animation):
            self.__surf = AnimationSet.new(animation, frame_speed)
        else: 
            self.__surf = animation
        self.__animation_active = True
    
    def attach_surface(self, surface: pg.Surface):
        self.__surf = surface
        self.__animation_active = False