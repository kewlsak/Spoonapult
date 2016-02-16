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
        print("Hello setup")

        #Angle
        self.lblAngle = Label(self, text="Angle")\
                        .grid(row=0, column=0, columnspan=2)
        self.sclAngle = Scale(self, to=0, from_=100, command=self.dummy, showval=0)\
                        .grid(row=1, column=0, columnspan=2)

        #Tension
        self.lblTension = Label(self, text="Tension")\
                          .grid(row=0, column=2, columnspan=2)
        self.sclTension = Scale(self, to=0, from_=100, command=self.dummy, showval=0)\
                          .grid(row=1, column=2, columnspan=2)

        #Rotation
        self.lblYaw = Label(self, text="Rotation")\
                      .grid(row=2, column=0, columnspan=4)
        #Major Left
        self.btnYawMajLeft = Button(self, text="<<", command=self.button_dummy)\
                             .grid(row=3, column=0)
        #Minor Left
        self.btnYawMinLeft = Button(self, text="<", command=self.button_dummy)\
                             .grid(row=3, column=1)
        #Minor Right
        self.btnYawMinRight = Button(self, text=">", command=self.button_dummy)\
                              .grid(row=3, column=2)
        #Major Right
        self.btnYawMinRight = Button(self, text=">>", command=self.button_dummy)\
                              .grid(row=3, column=3)
        
        
    def dummy(self, value):
        self.cat.changeAngle(int(value))
        print(self.cat.angle)
        pass

    def button_dummy(self):
        print("derp")
        


if __name__ == "__main__":
    root = Tk()
    control = TkCatapultControl(SimpleCatapult(), root)
    control.pack()
    root.mainloop()

    
           
