from ..game_object import GameObject

from ...utils import MAX_HP, MAX_MP, MATERIAL_CLASS, DEFAULT_MATERIAL_HEALTH


class Material(GameObject):
    """A class to represent a player in the game"""
    def __init__(self, color, init_pos, size, strength=DEFAULT_MATERIAL_HEALTH):
        super().__init__(*init_pos, *size, color, 0, HP=strength, MP=1)
        self.rect.centerx, self.rect.centery = init_pos 

    def typeIdentifier(self):
        return MATERIAL_CLASS


