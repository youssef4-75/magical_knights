


from abc import ABC, abstractmethod


class DisplayerABC(ABC):
    @abstractmethod
    def display(self, ):
        ...

    @property
    @abstractmethod
    def window(self):
        ...