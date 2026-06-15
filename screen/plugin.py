



from abc import ABC, abstractmethod

from .window_abc import WindowABC


class Plugin(ABC):

    @abstractmethod
    def activate(self, window: WindowABC):
        ...

    @abstractmethod
    def init(self, window: WindowABC):
        ...