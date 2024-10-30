#!/bin/python3

import keyboard

print("Running")

while True:
    pressed_key = keyboard.read_event()
    print(pressed_key.name)
    if pressed_key.name == "q":
        quit()
