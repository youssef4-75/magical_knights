
from ..essence.motion_mixin import MotionMixin


class ProjectileMM(MotionMixin):

    def advance_rect(self):
        super().advance_rect()
        self.move_in_direction(self.vel)
