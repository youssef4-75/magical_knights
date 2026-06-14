



from objects import GameObject
from utils import Vector


class Repeller:
    def repel(self, obj: GameObject, force: Vector):
        obj.set_accel(force)
