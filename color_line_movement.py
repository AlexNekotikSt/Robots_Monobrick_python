from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)

wheel_diameter = 56

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=114)

previous_color = None

drive_base.drive(100, 0)

while True:
    detected_color = color_sensor.color()
    
    if detected_color != previous_color:
        if detected_color == Color.RED:
            ev3.speaker.say("Red")
        elif detected_color == Color.BLUE:
            ev3.speaker.say("Blue")
        elif detected_color == Color.GREEN:
            ev3.speaker.say("Green")
        elif detected_color == Color.YELLOW:
            ev3.speaker.say("Yellow")
        elif detected_color == Color.BLACK:
            ev3.speaker.say("Stop")
            drive_base.stop()
            break
        elif detected_color == Color.WHITE:
            ev3.speaker.say("White")
        else:
            ev3.speaker.say("Unknown color")
        
        previous_color = detected_color
    
    wait(100)