#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)
ultrasonic = UltrasonicSensor(Port.S4)

wheel_diameter = 56

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

while True:
    detected_color = color_sensor.color()
    distance = ultrasonic.distance()
    
    if detected_color == Color.BLACK:
        drive_base.stop()
        drive_base.straight(-100)
        drive_base.turn(90)
    elif distance < 200:
        drive_base.drive(150, 0)
    else:
        drive_base.drive(50, 0)
    
    wait(100)