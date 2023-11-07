from lights.command import Command

class DecreaseBrightnessCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.decrease_brightness()
