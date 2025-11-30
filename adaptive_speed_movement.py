from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
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

# Continuously adjust speed based on ambient light
while True:
    # Get ambient light level (0-100)
    ambient_light = color_sensor.ambient()
    
    # Calculate speed proportional to light (e.g., 0-500 mm/s)
    speed = ambient_light * 5
    
    # Move forward with adjusted speed
    drive_base.drive(speed, 0)
    
    wait(100)  # Update every 100 ms