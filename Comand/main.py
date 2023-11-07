from lights.light import Light
from lights.turn_on_light_command import TurnOnLightCommand
from lights.turn_off_light_command import TurnOffLightCommand
from lights.increase_brightness_command import IncreaseBrightnessCommand
from lights.decrease_brightness_command import DecreaseBrightnessCommand
from lights.remote_control import RemoteControl

if __name__ == "__main__":
    light = Light()
    turn_on_command = TurnOnLightCommand(light)
    turn_off_command = TurnOffLightCommand(light)
    increase_brightness_command = IncreaseBrightnessCommand(light)
    decrease_brightness_command = DecreaseBrightnessCommand(light)

    remote_control = RemoteControl()
    remote_control.assign_command("ON", turn_on_command)
    remote_control.assign_command("OFF", turn_off_command)
    remote_control.assign_command("+", increase_brightness_command)
    remote_control.assign_command("-", decrease_brightness_command)

    remote_control.press_button("ON")
    remote_control.press_button("+")
    remote_control.press_button("+")
    remote_control.press_button("+")
    remote_control.press_button("-")
    remote_control.press_button("change channel")
