import tkinter 
from tkinter import *
import asyncio
from PIL import  ImageTk,Image
import SecileniCevir

class App:
    async def exec(self):
        
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()
        

class Window():

    def __init__(self, loop):
        root = Tk()
        root.geometry("740x340")

        image1 = Image.open("gri.jpg")
        img1 = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=img1,height = 300, width = 253)
        label1.image = img1
        label1.place(x=10, y=10)

        image2 = Image.open("test_image.png")
        img2 = ImageTk.PhotoImage(image2)
        label2 = tkinter.Label(image=img2,height = 280, width = 233)
        label2.image = img2
        label2.place(x=20, y=20)

        T = Text(root, height = 5, width = 52)
        T.place(x=300, y=230)

        Lb1 = Listbox(root,height = 10, width = 69)
        Lb1.place(x=300, y=15)

        root.mainloop()



asyncio.run(App().exec())