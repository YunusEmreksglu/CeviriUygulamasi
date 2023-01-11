import keyboard
import pyautogui
import re
import pytesseract 
from PIL import  ImageGrab
from googletrans import Translator
import numpy as np
import cv2 
import win32gui, win32ui
from tkinter import *
from tkinter import ttk
import asyncio

translator=Translator()

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

async def Form(x,y,yazi):

    root = Tk()
    root.iconify()
    root.attributes('-alpha', 0.0)
    frm = Toplevel(root)
    frm.geometry("150"+"x50+"+str(x)+"+"+str(y-100)) #Whatever size
    frm.overrideredirect(1) #Remove border

    ttk.Label(frm,text=yazi).place(x=10, y=25)
    btn=ttk.Button(frm,text="Çıkış",command=root.destroy).place(x=142, y=0)
    await frm.mainloop()

def printPressedKey(e):
    global tkr,xy1,xyA,xyAE,Cs
    if(tkr=='+'):
        Cs=0
        xy1=pyautogui.position()
        xyA=xy1
        xyAE=xyA
        tkr='-'
    else:
        xyAE=xyA
        xyA=pyautogui.position()
    """Cizgi()"""

def printreleaseKey(e):
    global tkr,xy2,dil
    xy2=pyautogui.position()
    tkr="+"
    try:
        win32gui.InvalidateRect(hwnd,None,True)
    except:
        print("")
    if (e.name=='alt'): 
        dil=["jpn","ja","J"]
    if(e.name=='ctrl'): 
        dil=["eng","en","E"]
        
    Ceviri()

def Ceviri():
    try:
        X=Bsayi(xy1[0],xy2[0])
        Y=Bsayi(xy1[1],xy2[1])
        img= ImageGrab.grab(bbox=(X[0],Y[0],X[1],Y[1]))
        img_np=np.array(img)
        img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        img.save('test_image.png') 

        b = pytesseract.image_to_string(img_final,lang =dil[0])
        """jpn/eng"""

        Normal = re.sub(r'\n', ' ', b)
        if(b!=""):
            print("\n"+Normal)
            Ceviri=translator.translate(Normal,src=dil[1],dest='tr').text
            print(Ceviri.replace('|','I'))
            Not(Ceviri,Normal,dil[2])
            """ja/en"""
        
            """asyncio.run(Form(X[0],Y[0],Meal))"""

        else:
            print("Yazı Bulunamadı")
    except:
        print("Bir Hata Aldın")
    
def Cizgi():
    global hwnd
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)

    """
    dcObj.SetBkColor(0xFF0000)
    dcObj.SetBkMode(1)
    """

    if(xyAE[0]!=xyA[0] and xyAE[1]!=xyA[1]):
        
        hwnd = win32gui.WindowFromPoint(( xy1[0],xy1[1]))
        win32gui.InvalidateRect(hwnd,None,True)
        
        """dcObj.Rectangle((xy1[0], xy1[1], xyA[0], xyA[1]))"""

        
        dcObj.Rectangle((xy1[0], xy1[1], xy1[0]+5, xyA[1]+5))

        dcObj.Rectangle((xy1[0],xy1[1] ,xyA[0]+5,xy1[1]+5))

        dcObj.Rectangle((xyA[0],xy1[1], xyA[0]+5,xyA[1]+5))

        dcObj.Rectangle((xy1[0],xyA[1], xyA[0]+5,xyA[1]+5))
        

        """
        win32gui.MoveToEx(dc,xy1[0],xy1[1])
        win32gui.LineTo(dc,xy1[0],xyA[1])

        win32gui.MoveToEx(dc,xy1[0],xy1[1])
        win32gui.LineTo(dc,xyA[0],xy1[1])

        win32gui.MoveToEx(dc,xyA[0],xy1[1])
        win32gui.LineTo(dc,xyA[0],xyA[1])

        win32gui.MoveToEx(dc,xy1[0],xyA[1])
        win32gui.LineTo(dc,xyA[0],xyA[1])
        """

def Bsayi(sayi1,sayi2):
    Sayi=["",""]
    if (sayi1>sayi2):
        Sayi=[sayi2,sayi1]
    if(sayi1<sayi2):
        Sayi=[sayi1,sayi2]

    return Sayi

def Not(CeviriT,NormalT,Dil):
    f = open("Ceviri("+Dil+").txt", "a",encoding='utf8')
    f.write("\n\nN: "+NormalT+" \n"+"C: "+CeviriT)
    f.close()

tkr='+'

keyboard.on_release_key('alt',printreleaseKey,suppress=False)
keyboard.on_release_key('ctrl',printreleaseKey,suppress=False)

keyboard.on_press_key('alt',printPressedKey,suppress=False)
keyboard.on_press_key('ctrl',printPressedKey,suppress=False)

print("Hazır")

while True:
    keyboard.wait()


    

