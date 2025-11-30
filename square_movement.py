#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.robotics import DriveBase
import math

# Create your objects here.
ev3 = EV3Brick()

# Define motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Wheel diameter in mm (standard LEGO wheel)
wheel_diameter = 56

# Calculate circumference
circumference = math.pi * wheel_diameter

# Create DriveBase
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

# Move in a square where each side equals the wheel circumference
for _ in range(4):
    drive_base.straight(circumference)
    drive_base.turn(90)