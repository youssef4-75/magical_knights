


from objects.game_object import GameObject
from types_tools import ObjectCreator
from ..container import ObjectsContainer


class LakeMixin:
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.lake: ObjectsContainer = ObjectsContainer()
    
    # lake
    def add(self, object_creator: ObjectCreator):
        return self.lake.add_to_me(object_creator)
    

    def append(self, *objects: GameObject):
        self.lake.add(*objects)
