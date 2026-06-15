




from container.ordered_lake import OrderedLake
from interaction_registry import InteractionsRegistryManager
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
        self.update()
        interacted = set()
        for axe in ["X", "Y"]:
            for p1, p2 in self.through_axe(axe):
                p1: GameObject; p2: GameObject
                if (p1, p2) not in interacted and p1.rect.colliderect(p2.rect):
                    interacted.add((p1, p2))
                    InteractionsRegistryManager.default(p1, p2)
                    InteractionsRegistryManager.map(p1.typeIdentifier(), p2.typeIdentifier())(p1, p2)
        
    def garbage_collect(self):
        removing: list[GameObject] = []
        for obj in self.objects:
            if not obj.is_alive():
                removing.append(obj)
        for _ in removing:
            self.objects.remove(_)
            _.die()