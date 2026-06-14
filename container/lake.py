



from typing import Any


class Lake[E]:
    def __init__(self, window, *objects: E) -> None:
        self.window = window
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

    def add_to_me(self, object_creator):
        o = object_creator()
        self.add(o)
        return o
