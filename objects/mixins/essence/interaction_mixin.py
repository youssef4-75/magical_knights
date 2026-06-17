
from typing import Any
from utils import Mixin


class InteractionMixin(Mixin):
    def __init__(self) -> None:
        self.__data: dict

    @staticmethod
    def start(self, **kwargs):
        self.__data = kwargs

    def get_IV(self, name: str):
        return self.__data.get(name)

    def set_IV(self, name: str, value: Any):
        self.__data[name] = value

    def add_IV(self, name: str, value: Any):
        if not name in self.__data:
            return
        self.__data[name] += value
