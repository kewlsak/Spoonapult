from Tkinter import Tk, Frame, Canvas, Checkbutton, Spinbox
import picamera
import io
import thread
import time
from PIL import Image, ImageTk

class TkPictureFrame(Frame):
    def __init__(self, x, y, master=None):
        Frame.__init__(self, master)
        self.photo = None
        self.resolution = (x, y)
        #The center of the Canvas is 0, 0. Find the center so
        #we can draw the image properly.
        self.center = ( x/2, y/2)
        #Setup the canvas
        self.picture = Canvas(self, width=x, height=y)
        #Place the canvas in the Grid.
        self.picture.grid(row=0,column=0,columnspan=2)
        #Camera check button control.
        self.checkButton = Checkbutton(self, text='Camera?',\
            command=self.toggleCamera)
        #Place it on the grid.
        self.checkButton.grid(row=1,column=0)
        #Spinbox to set FPS
        self.fpsSpin = Spinbox(self, text="FPS", from_=2, to=10,\
            command=self.fpsSpinCallback)
        self.fpsSpin.grid(row=1, column=1)
        #Set framerate
        self.fpsSpinCallback()
        #To determine if the camera is running
        self.capturing = False

    def fpsSpinCallback(self):
        self.fps = int(self.fpsSpin.get())

    def changePic(self, photo):
        #Make a reference to the old photo for removal
        self.oldphoto = self.photo
        #Setup the new photo
        self.photo = photo
        #Draw the new photo over the old photo
        self.picture.create_image(self.center,image=self.photo)
        #Remove the old photo
        self.picture.delete(self.oldphoto)
        #Enable the checkbox
        self.checkButton.config(state="normal")


    def timedDisable(self, widget):
        #Disable a widget for 2 seconds.
        widget.config(state="disabled")
        time.sleep(2)
        widget.config(state="normal")

    def threadTimeDisable(self, widget):
        #Run the timed disable in a thread to avoid lockups.
        thread.start_new_thread(self.timedDisable, (widget,))

    def startCamera(self):
        #Disable the checkbox and fps spinner.
        self.checkButton.config(state="disabled")
        self.fpsSpin.config(state="disabled")
        #Start the camera
        thread.start_new_thread(self.setupCamera, self.resolution)
        self.capturing = True

    def stopCamera(self):
        #Disable the checkbox for a duration.
        self.threadTimeDisable(self.checkButton)
        #Enable the spinner.
        self.fpsSpin.config(state="normal")
        #Clear the canvas.
        self.capturing = False
        self.picture.delete("all")
        

    def toggleCamera(self):
        if self.capturing:
            self.stopCamera()    
        else:
            self.startCamera()

    def setupCamera(self, x, y):
        with picamera.PiCamera() as camera:
            camera.resolution = (x, y)
            camera.framerate = self.fps
            stream = io.BytesIO()
            for each in camera.capture_continuous(stream, format='jpeg'):
                # Truncate the stream to the current position (in case
                # prior iterations output a longer image)
                each.truncate()
                #Rewind the stream
                each.seek(0)
                #Open the image stream and rotate is 180 degrees
                image = Image.open(each).transpose(Image.ROTATE_180)
                photo = ImageTk.PhotoImage(image)
                #Break out of the loop if not capturing
                if not self.capturing:
                    break
                #Update the canvas
                self.changePic(photo)
                #Reset playback to the beginning for the next image.
                each.seek(0)
                
                
                
                


if __name__ == "__main__":
    root = Tk()
      
    pictureframe = TkPictureFrame(400, 300, root)
    pictureframe.grid(row=0, column=0)
    
    
    root.mainloop()
    
