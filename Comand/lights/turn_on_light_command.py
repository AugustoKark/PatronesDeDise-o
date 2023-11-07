from lights.command import Command

class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()
