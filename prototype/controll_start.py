#!/usr/bin/python
### Based on left! But goes to right

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### Horizontal
Hor_A_1_pin = 23  # white
Hor_A_2_pin = 18  # black
Hor_B_1_pin = 15  # brown
Hor_B_2_pin = 14  # red

### Vertical
Ver_A_1_pin = 22  # gray
Ver_A_2_pin = 27  # purple
Ver_B_1_pin = 17  # blue
Ver_B_2_pin = 11  # green

# adjust if different
StepCount = 4#8
Seq = [[0, 0, 0, 0] for _ in range(StepCount)]
Seq[0] = [1, 0, 0, 0]
Seq[1] = [0, 1, 0, 0]
Seq[2] = [0, 0, 1, 0]
Seq[3] = [0, 0, 0, 1]

#Seq[0] = [1, 0, 0, 0]
#Seq[1] = [1, 1, 0, 0]
#Seq[2] = [0, 1, 0, 0]
#Seq[3] = [0, 1, 1, 0]
#Seq[4] = [0, 0, 1, 0]
#Seq[5] = [0, 0, 1, 1]
#Seq[6] = [0, 0, 0, 1]
#Seq[7] = [1, 0, 0, 1]
ratio = 25
delay = 2 / 1000.0
angle = 90

GPIO.setup(Hor_A_1_pin, GPIO.OUT)
GPIO.setup(Hor_A_2_pin, GPIO.OUT)
GPIO.setup(Hor_B_1_pin, GPIO.OUT)
GPIO.setup(Hor_B_2_pin, GPIO.OUT)

hor = [Hor_A_1_pin, Hor_A_2_pin, Hor_B_1_pin, Hor_B_2_pin]

GPIO.setup(Ver_A_1_pin, GPIO.OUT)
GPIO.setup(Ver_A_2_pin, GPIO.OUT)
GPIO.setup(Ver_B_1_pin, GPIO.OUT)
GPIO.setup(Ver_B_2_pin, GPIO.OUT)

ver = [Ver_A_1_pin, Ver_A_2_pin, Ver_B_1_pin, Ver_B_2_pin]


def set_step(w1, w2, w3, w4, pinout):
    GPIO.output(pinout[0], w1)
    GPIO.output(pinout[1], w2)
    GPIO.output(pinout[2], w3)
    GPIO.output(pinout[3], w4)


def forward(steps, pins):
    for i in range(steps):
        for j in range(StepCount):
            set_step(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3], pins)
            time.sleep(delay)


def backwards(steps, pins):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            set_step(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3], pins)
            time.sleep(delay)


steps = int(angle / (360 / ratio) * 4)#8)

