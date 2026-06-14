



from objects import GameObject
from utils import Vector, Singleton


class Repeller(Singleton):
    def repel(self, obj: GameObject, force: Vector):
        obj.set_accel(force)
