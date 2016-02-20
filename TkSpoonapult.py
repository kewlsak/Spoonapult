from TkCatapultControl import *
from TkPictureFrame import *
from ServoCatapult import *

if __name__ == "__main__":
    root = Tk()

    picture = TkPictureFrame(250, 176, root)
    picture.grid(row=0, column=0)
    
    #catapult = SimpleCatapult()
    catapult = ServoCatapult()
    #catapult.DEBUG = True
    control = TkCatapultControl(catapult, root)
    control.disableYaw()
    control.grid(row=1, column=0)
    root.mainloop()
