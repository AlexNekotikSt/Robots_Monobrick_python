from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()

# Define motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Define ultrasonic sensor
ultrasonic = UltrasonicSensor(Port.S4)

# Wheel diameter in mm (standard LEGO wheel)
wheel_diameter = 56

# Create DriveBase
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

# Maintain 15 cm (150 mm) distance from obstacle
target_distance = 150
tolerance = 10  # 10 mm tolerance

while True:
    distance = ultrasonic.distance()
    
    if distance > target_distance + tolerance:
        # Too far, move forward
        drive_base.drive(50, 0)
    elif distance < target_distance - tolerance:
        # Too close, move backward
        drive_base.drive(-50, 0)
    else:
        # Within range, stop
        drive_base.stop()
    
    wait(100)  # Update every 100 ms