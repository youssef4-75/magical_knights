
from typing import Any
from utils.mixin import Mixin


class InteractionMixin(Mixin):
    def __init__(self) -> None:
        self.__data: dict

    @staticmethod
    def start(self, **kwargs):
        self.__data = kwargs

    def get(self, name: str):
        return self.__data.get(name)

    def set(self, name: str, value: Any):
        self.__data[name] = value

    def add(self, name: str, value: Any):
        if not name in self.__data:
            return
        self.__data[name] += value
