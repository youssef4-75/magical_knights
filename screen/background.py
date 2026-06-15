
from pygame import Surface, image, transform

from screen.plugin import Plugin
from .window import Window


class WithBackGround(Plugin):
    def __init__(self, file_path) -> None:
        self.__file_path = file_path


    def activate(self, window: Window):
        window.screen.blit(self.__bg)

    def init(self, window: Window):
        self.__bg = image.load(self.__file_path)
        self.__bg = transform.scale(self.__bg, window.size())
        
    
    



