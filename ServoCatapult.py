from Catapult import *
from Servo import *
from time import sleep
import thread

class ServoCatapult(SimpleCatapult):
    def __init__(self):
        SimpleCatapult.__init__(self) #Run the superclass initialization method
        
        self.TENSION_SERVO_ADDRESS = 0
        self.ANGLE_SERVO_ADDRESS = 1
        self.YAW_SERVO_ADDRESS = 2
        self.LOCK_SERVO_ADDRESS = 3
       
        #Define the controller
        self.controller = ServoController(0x41)
        
        #Make reference to servos
        self.tension_servo = Servo(self.controller,self.TENSION_SERVO_ADDRESS)
        self.angle_servo = Servo(self.controller,self.ANGLE_SERVO_ADDRESS)
        self.yaw_servo = Servo(self.controller,self.YAW_SERVO_ADDRESS)
        self.lock_servo = Servo(self.controller,self.LOCK_SERVO_ADDRESS)

        #Servo thresholds
        self.TENSION_MIN = 60
        self.TENSION_MAX = 90
        self.ANGLE_MIN = 0
        self.ANGLE_MAX = 50
        self.YAW_MIN = 12
        self.YAW_MAX = 79

        #Servo presets
        self.NOTENSION = 0
        self.LOCKED = 0
        self.UNLOCKED = 50
        self.POST_LOCK_WAIT = 0.25
        self.POST_UNLOCK_WAIT = 0.5
        self.ANGLE_EASE_OFF_WAIT = 0.5
        self.ANGLE_EASE_OFF = 25

        #Defaults
        self.angle = (self.ANGLE_MIN + self.ANGLE_MAX)/2
        self.yaw = (self.YAW_MIN + self.YAW_MAX)/2
        self.tension = self.TENSION_MIN

        #Set initial servo position
        self.removeTension()
        self.applyAngle()
        self.applyYaw()
        self.removeLock()

        #Timed Disarm Thread
        seconds = 15
        self.count = seconds * 10
        self.timedDisarmPreExec = None #should be set externally
        self.timedDisarmPostExec = None #should be set externally
        self.timedDisarmBreak = False

    #override
    def __repr__(self):
        return (SimpleCatapult.__repr__(self))

    #override
    def applyAngle(self):
        if self.angle < self.ANGLE_MIN:
            self.angle = self.ANGLE_MIN
        elif self.angle > self.ANGLE_MAX:
            self.angle = self.ANGLE_MAX
        SimpleCatapult.applyAngle(self)
        self.angle_servo.changePositionPercent(self.angle)

    #override
    def applyYaw(self):
        if self.yaw < self.YAW_MIN:
            self.yaw = self.YAW_MIN
        elif self.yaw > self.YAW_MAX:
            self.yaw = self.YAW_MAX
        SimpleCatapult.applyYaw(self)
        self.yaw_servo.changePositionPercent(self.yaw)

    #override
    def applyTension(self):
        if self.tension < self.TENSION_MIN:
            self.tension = self.TENSION_MIN
        elif self.tension > self.TENSION_MAX:
            self.tension = self.TENSION_MAX
        SimpleCatapult.applyTension(self)
        self.tension_servo.changePositionPercent(self.tension)


    #override
    def removeTension(self):
        angle = self.angle
        SimpleCatapult.removeTension(self)
        if self.angle > self.ANGLE_EASE_OFF:
            self.angle = self.ANGLE_EASE_OFF
            self.applyAngle()
            sleep(self.ANGLE_EASE_OFF_WAIT)
        self.tension_servo.changePositionPercent(self.NOTENSION)
        self.angle = angle
        self.applyAngle()

    #override
    def applyLock(self):
        SimpleCatapult.applyLock(self)
        self.lock_servo.changePositionPercent(self.LOCKED)
        sleep(self.POST_LOCK_WAIT)
        self.timedDisarmBreak = False
        thread.start_new_thread(self.timedDisarm, (None,))

    #override
    def removeLock(self):
        self.timedDisarmBreak = True
        SimpleCatapult.removeLock(self)
        self.lock_servo.changePositionPercent(self.UNLOCKED)
        sleep(self.POST_UNLOCK_WAIT)

    #This method is used to disarm the catapult if it has been armed for
    #the time threshold of self.count * 0.1 seconds. The purpose of this
    #method is to reduce the stress on the tension servo by only allowing
    #it to be in a tense position for a short duration. The catapult is
    #disarmed after the time threshold is reached.
    #The method also has provision to call a user defined pre-method and
    #post-method to allow for handling of the disarm. For example, these
    #pre and post methods can be used by an UI to lock specific UI actions
    #until the disarm method is complete.
    def timedDisarm(self, junk):
        count = 0
        while count <= self.count:
            if self.timedDisarmBreak:
                if self.DEBUG:
                    print("SimpleCatapult.timedDisarm received exit signal.")
                return
            count += 1
            time.sleep(0.1)
        try:
            self.timedDisarmPreExec()
        except:
            if self.DEBUG:
                print("Warning: ServoCatapult.timedDisarm.PreExec not callable.")
        self.disarm()
        try:
            self.timedDisarmPostExec()
        except:
            if self.DEBUG:
                print("Warning: ServoCatapult.timedDisarm.PostExec not callable.")

