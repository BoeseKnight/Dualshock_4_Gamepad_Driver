from enum import Enum
import pygame


class Gamepad:
    controller = None

    @classmethod
    def run(cls):
        pygame.init()
        pygame.joystick.init()
        cls.controller=pygame.joystick.Joystick(0)
        cls.controller.init()


class GamepadButtons(Enum):
    # AXIS_LEFT_STICK_X = 0
    # AXIS_LEFT_STICK_Y = 1
    # AXIS_RIGHT_STICK_X = 2
    # AXIS_RIGHT_STICK_Y = 3
    # AXIS_R2 = 5
    # AXIS_L2 = 4

    CROSS = 0  # correct
    CIRCLE = 1  # correct
    SQUARE = 2  # correct
    TRIANGLE = 3  # correct

    SHARE = 4  # correct
    PS = 5  # correct
    OPTIONS = 6  # correct

    LEFT_STICK = 7  # correct
    RIGHT_STICK = 8  # correct

    L1 = 9  # correct
    R1 = 10  # correct
    # BUTTON_L2 =
    # BUTTON_R2 =

    ARROW_UP = 11  # correct
    ARROW_DOWN = 12  # correct
    ARROW_LEFT = 13  # correct
    ARROW_RIGHT = 14  # correct

    BUTTON_PAD = 15  # correct


class GamepadCommand:
    def __init__(self, button_number, button_name):
        self.button_number = button_number
        self.button_name = button_name

    def __str__(self):
        return f"{self.button_name}[{self.button_number}] pressed"
