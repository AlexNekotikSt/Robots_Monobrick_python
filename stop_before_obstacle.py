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

# Move forward until 15 cm (150 mm) from obstacle
drive_base.drive(100, 0)  # Speed 100 mm/s, straight
while ultrasonic.distance() > 150:
    wait(10)

# Stop when 15 cm from obstacle
drive_base.stop()