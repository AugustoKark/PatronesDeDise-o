from lights.command import Command

class IncreaseBrightnessCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.increase_brightness()
