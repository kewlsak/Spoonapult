from Tkinter import Tk, Frame, Canvas
import picamera
import io
import thread
from PIL import Image, ImageTk

class TkPictureFrame(Frame):
    def __init__(self, x, y, master=None):
        Frame.__init__(self, master)
        self.photo = None
        #The center of the Canvas is 0, 0. Find the center so
        #we can draw the image properly.
        self.center = ( x/2, y/2)
        #Setup the canvas
        self.picture = Canvas(self, width=x, height=y)
        #Place the canvas in the Grid.
        self.picture.grid(row=0,column=0)
        #Start the picamera capture thread.
        thread.start_new_thread(self.setupCamera, (x,y))

    def changePic(self, photo):
        #Make a reference to the old photo for removal
        self.oldphoto = self.photo
        #Setup the new photo
        self.photo = photo
        #Draw the new photo over the old photo
        self.picture.create_image(self.center,image=self.photo)
        #Remove the old photo
        self.picture.delete(self.oldphoto)
        

    def setupCamera(self, x, y):
        with picamera.PiCamera() as camera:
            camera.resolution = (x, y)
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
                self.changePic(photo)
                #Reset playback to the beginning for the next image.
                each.seek(0)
                
                
                


if __name__ == "__main__":
    root = Tk()
      
    pictureframe = TkPictureFrame(400, 300, root)
    pictureframe.grid(row=0, column=0)
    root.mainloop()
    
