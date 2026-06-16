
from pygame import Rect, image, transform
from game.plugin import Plugin



class WithBackGround(Plugin):
    def __init__(self, file_path) -> None:
        self.__file_path = file_path

    def activate(self, game):
        game.draw(self.__bg, Rect(0, 0, *game.screen_size))

    def init(self, game):
        self.__bg = image.load(self.__file_path)
        self.__bg = transform.scale(self.__bg, game.screen_size)

    



