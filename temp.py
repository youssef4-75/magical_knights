from typing import Callable


class A(Callable):
    def __init__(self, function):
        self.__core = function

    def __call__(self, *args, **kwargs):
        print("from a")
        self.__core(*args, **kwargs)

def deco(message):
    
    def deco_(function):
        def _(*args, **kwargs):
            print("from deco", message)
            return function(*args, **kwargs)
        return _
    return deco_


def Aify(function):
    return A(function)

@deco(1)
@deco(2)
@deco(3)
@Aify
def testing():
    print("from testing")

testing()