import pygame
import os
from gamepad import GamepadButtons, GamepadCommand, Gamepad

axis = {}
button = {}
Gamepad.run()
# Axes and buttons initialization
for i in range(Gamepad.controller.get_numaxes()):
    axis[i] = 0.0
for i in range(Gamepad.controller.get_numbuttons()):
    button[i] = False

print("Press PS button to quit:", quit)
quit = False
while quit is False:
    isAction = False
    exact_event = None
    while isAction is False and exact_event is None:
        # Get events
        gamepad_events = pygame.event.get()

        for event in gamepad_events:
            if event.type == pygame.JOYAXISMOTION:
                axis[event.axis] = round(event.value, 3)
                # isAction = True
                # exact_event = event.axis
            elif event.type == pygame.JOYBUTTONDOWN:
                button[event.button] = True
                isAction = True
                exact_event = event.button
            elif event.type == pygame.JOYBUTTONUP:
                button[event.button] = False

    quit = button[GamepadButtons.PS.value]
    action = GamepadCommand(exact_event, GamepadButtons(exact_event).name)
    print(action)

    # Limited to 30 frames per second to make the display not so flashy
    clock = pygame.time.Clock()
    clock.tick(30)

# """
# Gamepad Module
# Daniel J. Gonzalez
# dgonz@mit.edu
#
# Based off code from: http://robots.dacloughb.com/project-1/logitech-game-pad/
# """
# import os
#
# import pygame
#
# pygame.init()
# j = pygame.joystick.Joystick(0)
# j.init()
# print('Initialized Joystick : %s' % j.get_name())
#
#
# def get():
#     out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0]
#     it = 0  # iterator
#     pygame.event.pump()
#
#     # Read input from the two joysticks
#     for i in range(0, j.get_numaxes()):
#         out[it] = j.get_axis(i)
#         it += 1
#     # Read input from buttons
#     for i in range(0, j.get_numbuttons()):
#         out[it] = j.get_button(i)
#         it += 1
#     return out
#
#
# while True:
#     print(*get(), sep='\n')
#     os.system('cls')
#     clock = pygame.time.Clock()
#     clock.tick(10)
#
# """
# Returns a vector of the following form:
# [LThumbstickX, LThumbstickY, Unknown Coupled Axis???,
# RThumbstickX, RThumbstickY,
# Button 1/X, Button 2/A, Button 3/B, Button 4/Y,
# Left Bumper, Right Bumper, Left Trigger, Right Triller,
# Select, Start, Left Thumb Press, Right Thumb Press]
#
# Note:
# No D-Pad.
# Triggers are switches, not variable.
# Your controller may be different
# """
