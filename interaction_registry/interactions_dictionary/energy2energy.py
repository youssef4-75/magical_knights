

from ...utils import ENERGY_CLASS
from ...objects import Energy

from .tools import register

@register(ENERGY_CLASS, ENERGY_CLASS)
def Energy2Energy(energy1: Energy, energy2: Energy):
    cons = min(energy1.MP, energy2.MP)

    energy1.consume(cons)
    energy2.consume(cons)