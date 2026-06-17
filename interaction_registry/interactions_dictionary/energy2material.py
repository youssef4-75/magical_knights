


from .tools import reclassify, register
from ...utils import ENERGY_CLASS, MATERIAL_CLASS
from ...objects import Energy, Material

@register(MATERIAL_CLASS, ENERGY_CLASS)
def Energy2Material(_material: Material, _energy: Energy):
    material, energy = reclassify(_material, _energy, _1st_class=Material, _2nd_class=Energy)
    material.damage(energy.MP)
    energy.consume(energy.MP)