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

# Continuous movement with obstacle avoidance
while True:
    # Move forward
    drive_base.drive(200, 0)  # Speed 200 mm/s, straight
    while ultrasonic.distance() > 200:
        wait(10)
    
    # Stop when obstacle detected
    drive_base.stop()
    
    # Move backward 200 mm
    drive_base.straight(-200)
    
    # Turn right 90 degrees
    drive_base.turn(90)
    
    # Continue to next obstacle