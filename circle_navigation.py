from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import math

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)

wheel_diameter = 56

circumference = math.pi * wheel_diameter

backward_distance = 2 * circumference

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

while True:
    drive_base.drive(100, 0)
    while color_sensor.color() != Color.BLACK:
        wait(10)
    
    drive_base.stop()
    
    drive_base.straight(-backward_distance)
    
    drive_base.turn(90)