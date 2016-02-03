from Tkinter import *
from ServoCatapult import *

############
#Initialize#
############

#Initialize the interface. MUST BE DONE BEFORE USING TKINTER!
interface = Tk()

#Define the Catapult
cat = ServoCatapult()

#Set debug output
cat.DEBUG = False



##################
#Callback Methods#
##################

###Trajectory Controls###
def angleCallBack(value):
    cat.changeAngle(int(value))

def yawCallBack(value):
    cat.changeYaw(int(value))

def tensionCallBack(value):
    cat.changeTension(int(value))

###Buttons###
def armCallBack():
    cat.arm()

def fireCallBack():
    cat.fire()


###################
#Keyboard Bindings#
###################

###Keyboard Callbacks

increment = 1

def keyUp(event): #Add to angle
    sclAngle.set(sclAngle.get()-increment)

def keyDown(event): #Subtract from angle
    sclAngle.set(sclAngle.get()+increment)

def keyLeft(event): #Add to yaw
    sclYaw.set(sclYaw.get()+increment)

def keyRight(event): #Subtract from yaw
    sclYaw.set(sclYaw.get()-increment)

def keySpace(event): #Fire the catapult
    fireCallBack()

def keyReturn(event): #Arm the catapult
    armCallBack()

def keyMinus(event): #Subtract from tension
    sclTension.set(sclTension.get()-increment)

def keyEqual(event): #Add to tension
    sclTension.set(sclTension.get()+increment)

###Keyboard Bindings###
interface.bind("<Up>", keyUp) #More angle
interface.bind("<Down>", keyDown) #Less angle
interface.bind("<Left>", keyLeft) #Less Yaw
interface.bind("<Right>", keyRight) #More Yaw
interface.bind("<space>", keySpace) #FIRE!
interface.bind("<Return>", keyReturn) #Arm
interface.bind("<minus>", keyMinus) #Less tension
interface.bind("<equal>", keyEqual) #More tension



#################
#DEFINE CONTROLS#
#################

###Scales###

#Angle
lblAngle = Label(interface, text="Angle")
sclAngle = Scale(interface, from_=cat.ANGLE_MIN, to_=cat.ANGLE_MAX, showvalue=0, command=angleCallBack)
sclAngle.set(cat.angle)

#Yaw
lblYaw = Label(interface, text="Yaw")
sclYaw = Scale(interface, to=cat.YAW_MIN, from_=cat.YAW_MAX, orient=HORIZONTAL, showvalue=0, command=yawCallBack)
sclYaw.set(cat.yaw)

#Tension
lblTension = Label(interface, text="Tension")
sclTension = Scale(interface, to=cat.TENSION_MIN, from_=cat.TENSION_MAX, showvalue=0, command=tensionCallBack)
sclTension.set(cat.tension)

###Buttons###

#Arm
btnArm = Button(interface, text="Arm", command=armCallBack)

#Fire
btnFire = Button(interface, text="FIRE!", command=fireCallBack)



##################
#Interface Layout#
##################

#Interface layout, grid format
#
#           Angle   Tension
#           Scale   Scale
#
#               Yaw
#               Scale
#
#
#           Arm     FIRE!


###Top Row###
lblAngle.grid(row=0, column=0)
lblTension.grid(row=0, column=1)

###Second Row###
sclAngle.grid(row=1, column=0)
sclTension.grid(row=1, column=1)

###Third Row###
lblYaw.grid(row=2, column=0, columnspan=2)

###Fourth Row###
sclYaw.grid(row=3, column=0, columnspan=2)

###Fifth Row###
btnArm.grid(row=4, column=0)
btnFire.grid(row=4, column=1)



#################
#RUN APPLICATION#
#################

#Go!
interface.mainloop()
