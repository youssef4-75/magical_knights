from utils import Singleton
from .draw import Drawer
from .force.repeller import Repeller
from .translate.translater import Translator


class ServicesManager(Singleton):
    def __init__(self, drawer: Drawer, repeller: Repeller, translator: Translator) -> None:
        self.drawer = drawer
        self.repeller = repeller
        self.translator = translator

    def repel(self, *args, **kwargs):
        return self.repeller.repel(*args, **kwargs)

    def draw(self, *args, **kwargs):
        return self.drawer.draw(*args, **kwargs)

    def translate(self, *args, **kwargs):
        return self.translator.translate(*args, **kwargs)



