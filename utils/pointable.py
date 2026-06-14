

from abc import ABC, abstractmethod


class Pointable(ABC):
    @abstractmethod
    def x(self):...

    @abstractmethod
    def y(self):...