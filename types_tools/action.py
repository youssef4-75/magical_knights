


from typing import Any, Callable, TypeVar


GameObject = TypeVar('GameObject')
GameManager = TypeVar('GameManager')

Action = Callable[[GameObject, GameManager], Any]