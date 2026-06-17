from typing import Callable, TypeVar







GameObject = TypeVar('GameObject')
ObjectCreator = Callable[[], GameObject]