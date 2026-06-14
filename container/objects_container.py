




from objects import GameObject
from .lake import Lake


class ObjectsContainer(Lake):
    def __init__(self, window, *objects: GameObject) -> None:
        super().__init__(window, *objects)

    def __iter__(self):
        self.objects: list[GameObject]
        for i in self.objects:
            i.advance()
            yield i
    
