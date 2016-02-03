from Servo import *

controller = ServoController(0x41)

servo0 = Servo(controller,0)
servo1 = Servo(controller,1)
servo2 = Servo(controller,2)
servo3 = Servo(controller,3)

servos = (servo0, servo1, servo2, servo3)

for servo in servos:
    servo.changePositionPercent(50)
