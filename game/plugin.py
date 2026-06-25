



from abc import ABC, abstractmethod




class Plugin(ABC):

    @abstractmethod
    def activate(self, game):
        ...

    @abstractmethod
    def init(self, game):
        ...

    def behaviour(self, gobj):
        ...

    def interaction(self, gobj1, gobj2):
        ...