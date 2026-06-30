







from abc import ABC


class Mixin(ABC):
    @staticmethod
    def start(self, *args, **kwargs):...


    def set_constant(self, **kwargs):
        ...