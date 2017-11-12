from PIL import Image, ImageTk
import PIL.Image

from tkinter import *
from tkinter import filedialog


root = Tk()

def make_label(root, x, y, h, w, *args, **kwargs):
    f = Frame(root, height=h, width=w)
    f.pack_propagate(0)
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label
    
def load_file():
        root.fileName = filedialog.askopenfilename(filetypes=(("All files", "*.*"),))
        global leftimage
        leftimage = root.fileName

        image = PIL.Image.open(leftimage)
        resized_height = 1080 
        resized_width = 1920

        image = image.resize((resized_width, resized_height), PIL.Image.ANTIALIAS)
        image.save("finalleft.png")
        
        #-------------------------------#

        img = PIL.Image.open(leftimage)
        img = img.convert("RGBA")
        img.save('leftimage.ppm', 'ppm', quality=95)
        
        v = PIL.Image.open('leftimage.ppm').resize((305, 160), PIL.Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(v)
        
        label = make_label(root, 40, 40, 160, 305, image=ph,)
        label.image=ph

def load_second_file():
        root.fileName = filedialog.askopenfilename(filetypes=(("All files", "*.*"),))
        global rightimage
        rightimage = root.fileName

        image2 = PIL.Image.open(rightimage)
        resized_height2 = 1080 
        resized_width2 = 1920

        image2 = image2.resize((resized_width2, resized_height2), PIL.Image.ANTIALIAS)
        image2.save("finalright.png")
        
        #-------------------------------#

        img2 = PIL.Image.open(rightimage)
        img2 = img2.convert("RGBA")
        img2.save('rightimage.ppm', 'ppm', quality=95)
        
        v2 = PIL.Image.open('rightimage.ppm').resize((305, 160), PIL.Image.ANTIALIAS)
        ph2 = ImageTk.PhotoImage(v2)
        
        label2 = make_label(root, 445, 40, 160, 305, image=ph2,)
        label2.image=ph2
        

def opencontext2():
    filedialog


def combine_images():

    left_half = PIL.Image.open("finalleft.png")
    right_half = PIL.Image.open("finalright.png")

    WIDTH = left_half.size[0] + right_half.size[0]
    HEIGHT = left_half.size[1]

    new_image = PIL.Image.new("RGB", (WIDTH, HEIGHT))

    new_image.paste(left_half, (0, 0))
    new_image.paste(right_half, (left_half.size[0], 0))
    new_image.save("combined.png")
    

root.geometry('{}x{}'.format(800, 300))

root.resizable(False, False)

w = Canvas(root, width=410, height=300)
w.place(relx=.2, rely=.4, anchor="c")

w.create_rectangle(80, 65, 400, 235)
b = Button(root, text="Get Left-Side Image", command=load_file)
b.place(relx=.2, rely=.1, anchor="c")

w2 = Canvas(root, width=400, height=300)
w2.place(relx=.7, rely=.4, anchor="c")
b2 = Button(root, text="Get Right-Side Image", command=load_second_file)
b2.place(relx=.75, rely=.1, anchor="c")

w2.create_rectangle(80, 65, 400, 235)

b3 = Button(root, text="Create Dual Monitor Wallpaper", command=combine_images)
b3.place(relx=.5, rely=.8, anchor="c")

mainloop()

