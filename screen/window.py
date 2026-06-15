import pygame

from .plugin import Plugin
from .window_abc import WindowABC 


class Window(WindowABC):
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.plugins: list[Plugin] = []

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                yield event 

    def fill(self, color):
        self.screen.fill(color)

    def draw(self, surface, rect):
        self.screen.blit(surface, rect)

    def activate_plugins(self):
        for plug in self.plugins:
            plug.activate(self)

    def display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def stop(self): self.running = False
    
    def start(self): self.running = True

    def add_plugin(self, *plugins: Plugin):
        for plugin in plugins:
            plugin.init(self)
            self.plugins.append(plugin)

    def size(self):
        return self.width, self.height