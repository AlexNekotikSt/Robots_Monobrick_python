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

target_distance = 150
tolerance = 10

while True:
    distance = ultrasonic.distance()
    
    if distance > target_distance + tolerance:
        drive_base.drive(50, 0)
    elif distance < target_distance - tolerance:
        drive_base.drive(-50, 0)
    else:
        drive_base.stop()
    
    wait(100)