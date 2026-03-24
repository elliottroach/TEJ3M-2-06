"""
Created by Aimar Fernandez
Created on Mar 2026
This program rotates a servo 180 and back over and over
"""

import board
import digitalio
import time
import adafruit_hcsr04

# setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin = borad.GP9, echo_pin=board.GP10)

# infinte loop
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
