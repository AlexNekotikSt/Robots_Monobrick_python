#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()

# Define motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Define sensors
color_sensor = ColorSensor(Port.S3)
ultrasonic = UltrasonicSensor(Port.S4)

# Wheel diameter in mm (standard LEGO wheel)
wheel_diameter = 56

# Create DriveBase
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

# Robot Sumo behavior: stay in ring, find and push opponent out
while True:
    detected_color = color_sensor.color()
    distance = ultrasonic.distance()
    
    if detected_color == Color.BLACK:
        # Hit the ring boundary, back up and turn to stay inside
        drive_base.stop()
        drive_base.straight(-150)  # Back up 150 mm
        drive_base.turn(180)  # Turn around
    elif distance < 300:
        # Opponent detected, charge forward to push
        drive_base.drive(300, 0)  # High speed charge
    else:
        # No opponent, search by turning
        drive_base.drive(0, 50)  # Turn in place slowly
    
    wait(100)  # Update every 100 ms