from typing import Callable, TypeVar







GameObject = TypeVar('GameObject')
GameManager = TypeVar("GameManager")
Interaction = Callable[[GameObject, GameObject, GameManager], None]
