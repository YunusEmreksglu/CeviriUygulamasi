
from tkinter import *
from tkinter import ttk
import keyboard
import pyautogui

def Form(x,y):
    root = Tk()
    root.iconify()
    root.attributes('-alpha', 0.0)
    frm = Toplevel(root)
    frm.geometry("100"+"x500+"+str(x)+"+"+str(y)) #Whatever size
    frm.overrideredirect(1) #Remove border

    ttk.Label(frm,text="hello world").grid(column=0,row=0)
    ttk.Button(frm,text="Çıkış",command=root.destroy).grid(column=1,row=1)
    frm.mainloop()

 
def printPressedKey(e):
    global tkr,xy1
    if(tkr=='+'):
        print("bastın")
        xy1=pyautogui.position()
        tkr='-'
    
    
def printreleaseKey(e):
    global tkr,xy2
    print("kaldırdın")
    xy2=pyautogui.position()
    tkr="+"
    Form(xy1[0],xy1[1])
    print(str(xy1[0])+" "+str(xy1[1])+" "+str(xy2[0])+" "+str(xy2[1])+" ")
 
tkr='+'
keyboard.on_release_key('alt',printreleaseKey,suppress=False)
keyboard.on_press_key('alt',printPressedKey,suppress=False)
 
while True:
    keyboard.wait()
    


