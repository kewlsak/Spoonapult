from Adafruit_PWM_Servo_Driver import *

class ServoController:
    def __init__(self, address):
        self.address = address
        self.frequency = 60 #most servos operate at 50Hz, however these ones are 60 for some unknown reason to me.

        #Setup the controller
        self.pwm = PWM(self.address)
        self.pwm.setPWMFreq(self.frequency)

    def getFreq(self):
        return self.frequency


class Servo:
    def __init__(self, controller, address):
        self.controller = controller
        self.DEBUG = False
        
        #Constants
        self.POS_MIN = 150 #Tick value based off of tests at 60Hz (absolute min 145)
        self.POS_MAX = 650 #Tick value based off of tests at 60Hz (absolute max 660)
        
        
        self.POS_NEUTRAL = float(( self.POS_MAX + self.POS_MIN ) /2.0)

        #Variables
        self.address = address #Address of the servo to control.
        self.pos = self.POS_NEUTRAL #Set the initial position.

        #Setup the servo
        #add code to setup the servo

    def __repr__(self):
        return "<%s " % self.__class__.__name__ + \
               "controller: %s TICK_MAX: %s POS_MIN: %s POS_NEUTRAL: %s POS_MAX: %s address: %s pos: %s" \
               % (self.controller, self.TICK_MAX, self.POS_MIN, self.POS_NEUTRAL, self.POS_MAX, self.address, self.pos) +\
               ">"    

    #Helper method to properly set the pos member. Must be integer and between the min/max.
    def setPos(self, pos):
        if type(pos) == int and (pos >= self.POS_MIN) and (pos <= self.POS_MAX):
            self.pos = pos

    #Apply the position to the servo
    def applyPos(self):
        if self.DEBUG:
            print("Applying position to servo: %s" % self.pos)
        self.controller.pwm.setPWM(self.address, 0, self.pos)


    #PUBLIC METHODS

    #Change position based off of a percentage (0 to 100), integers only.
    def changePositionPercent(self, percent):
        percent = float(percent) #make it a float

        percent = percent / 100.0
        if percent > 100.0:
            percent = 100.0

        offset = float(self.POS_MAX - self.POS_MIN) #the difference between max and min.
        tick = int(offset * percent) #Convert percentage to a duty cycle
        self.setPos(self.POS_MIN+tick) #Calc tick, then apply to pos.

        self.applyPos() #apply position to servo

    #Useful for setting to min, neutral, or max positions.        
    def changePositionTick(self, tick):
        self.setPos(tick)
        self.applyPos() #apply position to servo

    def changePositionAngle(self, angle):
        pass #add code to an angle in degrees.
            
