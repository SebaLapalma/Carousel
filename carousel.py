from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carousel')

img1 = ImageTk.PhotoImage(Image.open('images/image1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/image2.png'))
img3 = ImageTk.PhotoImage(Image.open('images/image3.png'))

list = [img1, img2, img3]

l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

def back(img_num):
    global l
    global btn_back
    global btn_foward
    
    l.grid_forget()
    
    l = Label(root, image=list[img_num])
    btn_back = Button(root, text=' < ', command=lambda:back(img_num-1))
    btn_foward = Button(root, text=' > ', command=lambda:foward(img_num+1))
    
    if img_num == 0:
        btn_back = Button(root, text='N/A', state=DISABLED)
    l.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_foward.grid(row=1, column=2)
    
def foward(img_num):
    global l
    global btn_back
    global btn_foward
    
    l.grid_forget()
    
    l = Label(root, image=list[img_num])
    btn_back = Button(root, text=' < ', command=lambda:back(img_num-1))
    btn_foward = Button(root, text=' > ', command=lambda:foward(img_num+1))
    
    if img_num == 2:
        btn_foward = Button(root, text='N/A', state=DISABLED)
    l.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_foward.grid(row=1, column=2)

btn_back = Button(root, text='N/A', state=DISABLED)
btn_foward = Button(root, text=' > ', command=lambda:foward(1))

btn_back.grid(row=1, column=0)
btn_foward.grid(row=1, column=2)

root.mainloop()