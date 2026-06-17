from types_tools import ObjectCreator


def consolify(up, down, left, right):
    return {
            "up": up,
            "down": down,
            "left": left,
            "right": right,
        }


def actionify(grimoire: dict, *keys, mana, cooldown, initial_delay, action):
    grimoire[keys, mana, cooldown, initial_delay] = action
    

def actionify_deco(grimoire: dict, *keys, mana, cooldown, initial_delay):
    def deco(action):
        actionify(grimoire, *keys, mana=mana, cooldown=cooldown, initial_delay=initial_delay, action=action)
        return action
    return deco 


def attach_grimoire[P](grimoire):
    def deco(function: ObjectCreator[P]):
        def result():
            p = function()
            p.add_actions(
                grimoire
            )
            return p
        return result
    return deco 