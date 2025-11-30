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

# Kegelring behavior: push pins out of the ring (white field bounded by black circle)
while True:
    detected_color = color_sensor.color()
    distance = ultrasonic.distance()
    
    if detected_color == Color.BLACK:
        # Hit the black boundary, back up and turn
        drive_base.stop()
        drive_base.straight(-100)  # Back up 100 mm
        drive_base.turn(90)  # Turn 90 degrees
    elif distance < 200:
        # Obstacle (pin) detected, push it forward
        drive_base.drive(150, 0)  # Faster speed to push
    else:
        # No obstacle, move forward slowly
        drive_base.drive(50, 0)
    
    wait(100)  # Update every 100 ms