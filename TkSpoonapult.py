from TkCatapultControl import *
from ServoCatapult import *

if __name__ == "__main__":
    root = Tk()
    catapult = SimpleCatapult()
    #catapult = ServoCatapult()
    catapult.DEBUG = True
    control = TkCatapultControl(catapult, root)
    control.grid(row=1, column=0)
    root.mainloop()
