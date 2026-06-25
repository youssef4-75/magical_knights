

from typing import Callable, TypeVar


from ..container import ObjectsContainer

from ...objects import GameObject
from ...types_tools import ObjectCreator, Interaction


class LakeMixin:
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.lake: ObjectsContainer = ObjectsContainer()
    
    # lake
    def add(self, object_creator: ObjectCreator):
        return self.lake.add_to_me(object_creator)
    

    def append(self, *objects: GameObject):
        self.lake.add(*objects)

    def add_default_interactions_lakeM(self, *interactions: Interaction):
        self.lake.add_interaction(*interactions)