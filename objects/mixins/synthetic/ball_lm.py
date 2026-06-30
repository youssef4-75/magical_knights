


from game_env import GameManager, LifeMixin




class BallLM(LifeMixin):
    def set_constant_lm(self, *, WIDTH):
        self.__WIDTH = WIDTH

    def is_alive(self):
        return not (self.rect.right < 0 or self.rect.left > self.__WIDTH) and self.HP > 0

    def init_outs(self):
        if not hasattr(self, "outs"):
            self.outs = 0
    
    @property
    def result(self):
        self.init_outs()
        return getattr(self, "outs")
    
    def die(self, game: GameManager):
        self.outs += 1
        game.add(lambda : self.copy_me())

    def copy_result(self, other: 'BallLM'):
        self.init_outs()
        self.outs = other.outs