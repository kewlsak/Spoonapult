from Tkinter import *
from Catapult import *

class TkCatapultControl(Frame):
    def __init__(self, catapult, master=None):
        if not isinstance(catapult, SimpleCatapult):
            raise TypeError("catapult is not of type SimpleCatapult")
        Frame.__init__(self, master)
        self.cat = catapult
        self.setup()

    def setup(self):

        #Angle
        Label(self, text="Angle").grid(row=0, column=0, columnspan=2)
        self.sclAngle = Scale(self, from_=self.cat.ANGLE_MIN, to=self.cat.ANGLE_MAX,\
                              command=self.angleCallBack, showval=0)
        self.sclAngle.set(self.cat.angle)
        self.sclAngle.grid(row=1, column=0, columnspan=2)

        #Tension
        Label(self, text="Tension").grid(row=0, column=2, columnspan=2)
        self.sclTension = Scale(self, to=self.cat.TENSION_MIN, from_=self.cat.TENSION_MAX,\
                                command=self.tensionCallBack, showval=0)
        self.sclTension.set(self.cat.tension)
        self.sclTension.grid(row=1, column=2, columnspan=2)

        #Rotation
        Label(self, text="Rotation").grid(row=2, column=0, columnspan=4)
        #Major Left
        Button(self, text="<<", command=self.majorLeftYawCallback)\
                     .grid(row=3, column=0)
        #Minor Left
        Button(self, text="<", command=self.minorLeftYawCallback)\
                             .grid(row=3, column=1)
        #Minor Right
        Button(self, text=">", command=self.minorRightYawCallback)\
                              .grid(row=3, column=2)
        #Major Right
        Button(self, text=">>", command=self.majorRightYawCallback)\
                              .grid(row=3, column=3)

        #Seperater
        Label(self).grid(row=4, column=0, columnspan=4)
        
        #Arm
        Button(self, text="Arm", command=self.armCallback)\
                     .grid(row=5, column=0, columnspan=2)

        #Fire
        Button(self, text="FIRE!", command=self.fireCallback)\
                     .grid(row=5, column=2, columnspan=2)

    
    def angleCallBack(self, value):
        self.cat.changeAngle(int(value))

    def tensionCallBack(self, value):
        self.cat.changeTension(int(value))

    major_increment = 10
    minor_increment = 1

    def majorLeftYawCallback(self):
        self.cat.changeYaw(self.cat.yaw + self.major_increment)

    def minorLeftYawCallback(self):
        self.cat.changeYaw(self.cat.yaw + self.minor_increment)

    def majorRightYawCallback(self):
        self.cat.changeYaw(self.cat.yaw - self.major_increment)

    def minorRightYawCallback(self):
        self.cat.changeYaw(self.cat.yaw - self.minor_increment)
       
    def armCallback(self):
        self.cat.arm()

    def fireCallback(self):
        self.cat.fire()

if __name__ == "__main__":
    root = Tk()
    catapult = SimpleCatapult()
    catapult.DEBUG = True
    control = TkCatapultControl(catapult, root)
    control.pack()
    root.mainloop()

    
           
