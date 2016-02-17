from Tkinter import Tk, Frame, Label

class TkPictureFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.picture = Label(self)
        self.picture.grid(row=0,column=0)

    def changePic(self, photo):
        self.photo = photo
        self.picture["image"] = self.photo


if __name__ == "__main__":
    root = Tk()
      
    pictureframe = TkPictureFrame(root)
    pictureframe.grid(row=0, column=0)
    root.mainloop()
    
