

from typing import Callable

from .object_creator import GameObject


Behaviour = Callable[[GameObject], None]