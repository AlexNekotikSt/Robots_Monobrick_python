from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()

# Define motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Define color sensor
color_sensor = ColorSensor(Port.S3)

# Wheel diameter in mm (standard LEGO wheel)
wheel_diameter = 56

# Create DriveBase
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

# Move forward until black line is detected
drive_base.drive(100, 0)  # Speed 100 mm/s, straight
while color_sensor.color() != Color.BLACK:
    wait(10)

# Stop when black line is detected
drive_base.stop()