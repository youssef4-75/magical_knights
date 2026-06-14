



from typing import Any


class Lake[E]:
    def __init__(self, *objects: E) -> None:
        
        self.objects = list(objects)

    def add(self, *elements: E):
        for element in elements:
            self.objects.append(element)

    def handle(event):
        ...

    def __getitem__(self, index):
        return self.objects[index]

    def __iter__(self):
        for i in self.objects:
            yield i

    def __len__(self):
        return len(self.objects)