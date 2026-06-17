


from typing import Callable, Any


class Item(Callable):
    def __init__(self, class1, class2, function: Callable) -> None:
        self.__c1 = class1 
        self.__c2 = class2 
        self.__core = function

    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.__core(*args, **kwds)
    
    def extract(self):
        return self.__c1, self.__c2, self.__core

