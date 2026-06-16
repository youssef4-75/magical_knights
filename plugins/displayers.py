
from game import GameManager
from utils import PLAYER_CLASS

from game.plugin import Plugin
from ._player_displayer import PlayerDisplayer




class WithPDisplayer(Plugin):
    """
    Add displayers for HP for all player
    """

    def __init__(self) -> None:
        self.__displays: list[PlayerDisplayer] = []

    def activate(self, game: GameManager):
        for displayer in self.__displays:
            displayer.display()

    def init(self, game: GameManager):
        for index, p in enumerate(game.lake):

            if p.typeIdentifier() is not PLAYER_CLASS: 
                continue
            self.__displays.append(
                PlayerDisplayer.from_player(
                    p, game, index=index
                    )
                )