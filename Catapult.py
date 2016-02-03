#!/usr/bin/python3

##- USE -
##Import the Catapult class, instantiate an SimpleCatapult object,
##call the arm method, then fire! See below:
##
##>>> import Catapult
##>>> cat = Catapult.SimpleCatapult()
##>>> cat.arm()
##>>> cat.fire()
##
##- Public Members -
##-- VARIABLES --
##isArmed - boolean - used to determine if the catapult is armed
##DEBUG - boolean - set to True to enable debug output
##
##-- METHODS --
##arm() - arm the catapult
##disarm() - disarms the catapult
##fire() - fires the catapult
##changeTension() - changes the tension setting and applies it to the catapult
##changeAngle() - same as above but for angle
##changeYaw() - same as above but for yaw

##- Methods to Override -
##applyTension() - applies the tension setting to the catapult
##removeTension() - completely removes tension from the catapult
##applyLock() - engages the throwing arm lock.
##removeLock() - disengages the throwing arm lock.
##applyAngle() - applies the angle to the catapult.
##applyYaw() - applies the yaw to the catapult


class SimpleCatapult: 
    def __init__(self):
        #Constants
        self.scaleMin = 0
        self.scaleMax = 100
        
        #Defaults
        self.tension = 50
        self.angle = 50
        self.yaw = 50
        self.isArmed = False #Public
        self.isLocked = False
        self.isTense = False

        self.DEBUG = False #Public

    #Describe the object for the Python standard repr(obj) method.
    def __repr__(self):
        return "<%s scale:%s-%s tension:%s angle:%s " \
               % (self.__class__.__name__, self.scaleMin, self.scaleMax, self.tension, self.angle) \
               + "yaw:%s isArmed:%s isLocked:%s isTense:%s DEBUG:%s>" \
               % (self.yaw, self.isArmed, self.isLocked, self.isTense, self.DEBUG)

    def __str__(self):
        #Output the same as repr.
        return self.__repr__()

    #Check if a value is and integer and within scale.
    def checkValue(self, value):
        if  type(value) == int and \
            ( value >= self.scaleMin and value <= self.scaleMax ):
            check = True
                            
        else:
            check = False
            if self.DEBUG:
                print("The value", value,
                      "is not an integer, or is not between",
                      self.scaleMin, "and", self.scaleMax)
        return check

    #Reusable debug print statement methods for passes and failures.
    def debugPassSetVal(self, name, value):
        if self.DEBUG:
            print("Setting", name,"to:",value)

    def debugFailSetVal(self, name, value):
        if self.DEBUG:
            print("Unable to set",name,"to:",value)

    #Set the tension, angle, and Yaw of the catapult.
    #Do not mutate the member values on failure.
    
    #TENSION
    def setTension(self, tension):
        name = "tension"
        if self.checkValue(tension):
            self.tension = tension
            self.debugPassSetVal(name,tension)
        else:
            self.debugFailSetVal(name,tension)
    #ANGLE
    def setAngle(self, angle):
        name = "angle"
        if self.checkValue(angle):
            self.angle = angle
            self.debugPassSetVal(name,angle)
        else:
            self.debugFailSetVal(name,angle)
    #YAW
    def setYaw(self, yaw):
        name = "yaw"
        if self.checkValue(yaw):
            self.yaw = yaw
            self.debugPassSetVal(name,yaw)
        else:
            self.debugFailSetVal(name,yaw)

    #The apply methods will take the internal tension, angle,
    #yaw, and lock settings and apply them to the catapult.

    #debug print method
    def debugApplyValue(self,name,value):
        if self.DEBUG:
            print("Applied",value,"to",name)
                
    def applyTension(self): #Extend
        name = "tension"
        self.debugApplyValue(name,self.tension)
        
    def removeTension(self): #Extend
        name = "tension"
        zeroval = 0
        self.debugApplyValue(name,zeroval)

    def applyAngle(self): #Extend
        name = "angle"
        self.debugApplyValue(name,self.angle)
        
    def applyYaw(self): #Extend
        name = "yaw"
        self.debugApplyValue(name,self.yaw)

    def debugChangeVal(self,name,old,new):
        if self.DEBUG:
            print("Changing",name,"from",old,"to",new)

    def changeTension(self, value): #Public
        self.debugChangeVal("tension",self.tension,value)
        self.setTension(value)
        if self.isArmed:
            if self.DEBUG:
                print("Catapult is armed, applying tension...")
            self.applyTension()
            
    def changeAngle(self, value): #Public
        self.debugChangeVal("angle",self.angle,value)
        self.setAngle(value)
        self.applyAngle()

    def changeYaw(self,value): #Public
        self.debugChangeVal("yaw",self.yaw,value)
        self.setYaw(value)
        self.applyYaw()

    def toggleTension(self):
        name = "isTense"
        #Remove the tension if it is not of boolean type or if True,
        #otherwise apply the tension
        if (type(self.isTense) != bool) or self.isTense:
            self.removeTension()
            self.isTense = False
        else:
            self.applyTension()
            self.isTense = True
        self.debugApplyValue(name,self.isTense)

    def applyLock(self): #Extend
        name = "isLocked"
        self.isLocked = True
        self.debugApplyValue(name,self.isLocked)

    def removeLock(self): #Extend
        name = "isLocked"
        self.isLocked = False
        self.debugApplyValue(name,self.isLocked)

    def toggleLock(self):
        name = "isLocked"
        #Unlock if it is not of boolean type or if True,
        #Otherwise lock
        if (type(self.isLocked) != bool) or self.isLocked:
            self.removeLock()
        else:
            self.applyLock()  

    #Arm and disarm the catapult.
    def debugArmState(self,word):
        if self.DEBUG:
            print(word,"catapult")

    def debugRearm(self):
        if self.DEBUG:
            print("Catapult is already armed, re-arming...")
      
    def arm(self): #Public
        name = "Armed"
        #Disarm the catapult if its armed or if the state is unknown.
        if (type(self.isArmed) != bool) or self.isArmed:
            self.debugRearm()
            self.disarm()
        #Arm the catapult
        self.toggleLock()
        self.toggleTension()
        self.isArmed = True
        self.debugArmState(name)

    def disarm(self): #Public
        name = 'Disarmed'
        #Remove the tension
        if (type(self.isTense) != bool) or self.isTense:
            self.toggleTension()            
        #Remove the lock
        if (type(self.isLocked) != bool) or self.isLocked:
            self.toggleLock()

        self.isArmed = False
        self.debugArmState(name)
        

    def fire(self): #Public
        #Only fire if all the checks are True.
        if self.isArmed and self.isTense and self.isLocked:
            if self.DEBUG:
                print('FIRE!')
            self.toggleLock()
        else:
            if self.DEBUG:
                print('Catapult is not armed properly. Disarming...')
        #Disarm the catapult.
        self.disarm()
        
    
