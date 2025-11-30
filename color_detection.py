from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)

while True:
    detected_color = color_sensor.color()
    
    if detected_color == Color.RED:
        ev3.speaker.say("Red")
    elif detected_color == Color.BLUE:
        ev3.speaker.say("Blue")
    elif detected_color == Color.GREEN:
        ev3.speaker.say("Green")
    elif detected_color == Color.YELLOW:
        ev3.speaker.say("Yellow")
    elif detected_color == Color.BLACK:
        ev3.speaker.say("Black")
    elif detected_color == Color.WHITE:
        ev3.speaker.say("White")
    else:
        ev3.speaker.say("Unknown color")
    
    wait(1000)