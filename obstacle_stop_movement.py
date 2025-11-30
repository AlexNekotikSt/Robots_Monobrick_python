from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

ultrasonic = UltrasonicSensor(Port.S4)

wheel_diameter = 56

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

drive_base.drive(200, 0)
while ultrasonic.distance() > 200:
    wait(10)

drive_base.stop()