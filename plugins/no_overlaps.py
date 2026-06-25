


from ..interaction_registry import InteractionsRegistryManager
from ._player_displayer import PlayerDisplayer
from ..game import GameManager, Plugin
from ..utils import PLAYER_CLASS



class WithNoOverlaps(Plugin):
    def activate(self, game: GameManager):
        ...

    def init(self, game: GameManager):
        print("started this plugin")
        ...

    def interaction(self, gobj1, gobj2):
        return InteractionsRegistryManager.default(gobj1, gobj2)