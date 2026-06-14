


from exceptions import ReWriteCommandException


class ControlPannel:
    def __init__(self, up, down, left, right, **commands) -> None:
        self.directions = {
            "up": up,
            "down": down,
            "left": left,
            "right": right,
        }
        self.commands = commands 

    def add_command(self, key, command):
        if key in self.commands: 
            raise ReWriteCommandException("you are rewriting a command that is already defined")
        self.commands[key] = command 
