



from game_object import GameObject
from vector import Vector


class Repeller:
    def repel(self, obj: GameObject, force: Vector):
        obj.set_accel(force)
