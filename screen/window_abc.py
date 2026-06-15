


from abc import ABC


class WindowABC(ABC):
    def __init__(self, title, width, height):...

    def events(self):...

    def fill(self, color):...

    def draw(self, surface, rect):...

    def display(self):...

    def stop(self): self.running = False
    
    def start(self): self.running = True

    def add_plugin(self, plugin):...

    def size(self):...