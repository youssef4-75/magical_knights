




from container.ordered_lake import OrderedLake
from interaction_registry import InteractionsRegistry
from objects import GameObject


class ObjectsContainer(OrderedLake):
    def __init__(self, *objects: GameObject) -> None:
        super().__init__(*objects)

    def __iter__(self):
        self.objects: list[GameObject]
        for i in self.objects:
            i.advance()
            yield i

    def interaction(self):
        interacted = set()
        
        for p1, p2 in self.through_X():
            p1: GameObject; p2: GameObject
            if (p1, p2) not in interacted and p1.rect.colliderect(p2.rect):
                interacted.add((p1, p2))
                InteractionsRegistry.map(p1.typeIdentifier(), p2.typeIdentifier())(p1, p2)
            
        for p1, p2 in self.through_Y():
            p1: GameObject; p2: GameObject
            if (p1, p2) not in interacted and p1.rect.colliderect(p2.rect):
                interacted.add((p1, p2))
                InteractionsRegistry.map(p1.typeIdentifier(), p2.typeIdentifier())(p1, p2)
    
