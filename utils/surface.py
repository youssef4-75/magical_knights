import pygame as pg
from icecream import ic

from .vector import Vector

# def get_interaction_normal(rect1: pg.Rect, rect2: pg.Rect) -> Vector:
#     """
#     Get the normal direction of the interaction between two rectangles.
#     Returns a unit vector pointing from rect1 to rect2.
#     """
#     # Get centers
#     center1 = Vector(rect1.centerx, rect1.centery)
#     center2 = Vector(rect2.centerx, rect2.centery)
    
#     # Vector from rect1 to rect2
#     direction = center2 - center1
    
#     # Get overlap amounts on each axis
#     overlap_x = (rect1.width + rect2.width) / 2 - abs(rect1.centerx - rect2.centerx)
#     overlap_y = (rect1.height + rect2.height) / 2 - abs(rect1.centery - rect2.centery)
    
#     # Determine which axis has less overlap (the collision normal)
#     if overlap_x < overlap_y:
#         # Horizontal collision
#         if (direction.x > 0 and rect2.right < rect1.right) or (direction.x < 0 and rect2.left > rect1.left) :
#             normal = Vector(1, 0) if center2.x > center1.x else Vector(-1, 0)
#         else:
#             normal = direction if False else Vector(1, 0) if center2.x > center1.x else Vector(-1, 0)
#     else:
#         # Vertical collision
#         if (direction.y > 0 and rect2.bottom < rect1.bottom) or (direction.y < 0 and rect2.top > rect1.top) :
#             normal = Vector(0, 1) if center2.y > center1.y else Vector(0, -1)
#         else:
#             normal = direction if False else Vector(1, 0) if center2.x > center1.x else Vector(-1, 0)
    
#     return normal



def get_interaction_normal(rect1: pg.Rect, rect2: pg.Rect) -> Vector:
    """
    Get the normal direction of the interaction between two rectangles.
    Returns a unit vector pointing from rect1 to rect2.
    """
    # Get centers
    center1 = Vector(rect1.centerx, rect1.centery)
    center2 = Vector(rect2.centerx, rect2.centery)
    
    # Calculate distances
    dx = center2.x - center1.x
    dy = center2.y - center1.y
    
    # Calculate overlap
    overlap_x = (rect1.width + rect2.width) / 2 - abs(dx)
    overlap_y = (rect1.height + rect2.height) / 2 - abs(dy)
    
    # Determine normal based on minimum penetration
    if overlap_x < overlap_y:
        return Vector(1 if dx > 0 else -1, 0)
    else:
        return Vector(0, 1 if dy > 0 else -1)