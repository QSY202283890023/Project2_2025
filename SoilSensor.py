# !/usr/bin/python
# Program Title: soil sensor
# Program Decription: This script monitors soil moisture levels using a bbutton sensor on  Raspberry Pi.
# Name: Siyuan QIn
# Student ID:202283890023
# Course&Year: Project Semester 3 & Grade 3
# Date: 17/4/2025
from gpiozero import Button
import time

channel = 21

sensor = Button(channel)

def callback():
    if sensor.is_pressed:
        print("Water Detected! YES")
    else:
        print("Water Detected! NO")

sensor.when_pressed = callback
sensor.when_released = callback

while True:
    time.sleep(1)
