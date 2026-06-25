
from .lake_mixin import LakeMixin
from ...types_tools import Interaction, Behaviour

from ..plugin import Plugin

class PluginMixin: 
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.plugins: list[Plugin] = []
        self.behaviours: list[Behaviour] = []
        self.interactions: list[Interaction] = []

    # plugin
    def add_plugin(self, *plugins: Plugin):
        for plugin in plugins:
            plugin.init(self)
            self.add_default_behaviour_PluginM(plugin.behaviour)
            self.add_default_interaction_PluginM(plugin.interaction)
            self.plugins.append(plugin)
        self.to_lake_mixin(self.interactions)

    # plugin
    def activate_plugins(self):
        for plug in self.plugins:
            plug.activate(self)

        
    def add_default_interaction_PluginM(self, interaction: Interaction):
        self.interactions.append(interaction)
        return interaction 
     
    
    def add_default_behaviour_PluginM(self, behaviour: Behaviour):
        self.behaviours.append(behaviour)
        return behaviour

    def to_lake_mixin(self, interactions: list[Interaction]):
        assert isinstance(self, LakeMixin)
        self.add_default_interactions_lakeM(*interactions)

