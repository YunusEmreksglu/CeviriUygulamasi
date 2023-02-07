import keyboard
import pyautogui
import re
import pytesseract 
from PIL import  ImageGrab
from googletrans import Translator
import numpy as np
import cv2 
import win32gui, win32api, win32con
import tkinter  as tk
from tkinter import *
from tkinter import ttk
import pystray
import PIL.Image
from array import *
import datetime

import Kütüphane.DilKutuphanesi as DilKutuphanesi

translator=Translator()

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image = PIL.Image.open("translateicon.jpg")

Durumu="başlatılıyor"
DilAyarlari=DilKutuphanesi.DilAyarlari(0) ## tr [0] / jp [1]
Diller=DilAyarlari[5]
DilBiligileri=DilKutuphanesi.CeviriDilBilgileri()
CeviriDili=DilBiligileri[1]
Acik=True
enbl=False


def ayarlar():
    def ComboxS(event):
        global CeviriDili
        a=0
        for x in Diller :
            if(SecilenDil.get()==x):
                CeviriDili=DilBiligileri[a]
            a=a+1
        iconUpdate()

    root = tk.Tk()
    root.geometry('300x300')
    root.resizable(False, False)
    root.title(DilAyarlari[2])
    
        

    SecilenDil=tk.StringVar()

    Combobx=ttk.Combobox(root, values=Diller,state="readonly",textvariable=SecilenDil)
    Combobx.set(Diller[int(CeviriDili[3])])
    Combobx.place(relx=0.5, rely=0.45,anchor=CENTER)
    Combobx.bind('<<ComboboxSelected>>', ComboxS)

  
    ##btn=ttk.Button(root, text="Çıkış",command=root.quit())
    ##btn.place(relx=0.5, rely=0.65,anchor=CENTER)

    root.mainloop()

def printPressedKey(e):
    if("başlatılıyor"==Durumu):
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
        #Cizgi()

def printreleaseKey(e):
    if("başlatılıyor"==Durumu):
        global tkr,xy2,dil
        xy2=pyautogui.position()
        tkr="+"
        try:
            win32gui.InvalidateRect(hwnd,None,True)
        except:
            print("")
        dil=CeviriDili
        Ceviri()

def Ceviri():
    try:
        X=Bsayi(xy1[0],xy2[0])
        Y=Bsayi(xy1[1],xy2[1])
        img= ImageGrab.grab(bbox=(X[0],Y[0],X[1],Y[1]),all_screens=True)
        img_np=np.array(img)
        img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        img.save('test_image.png') 

        b = pytesseract.image_to_string(img_final,lang =dil[0])
        """jpn/eng"""

        Normal = re.sub(r'\n', ' ', b).replace('|','I')
        if(b!=""):
            print("\n"+Normal)
            Ceviri=translator.translate(Normal,src=dil[1],dest=DilAyarlari[6]).text
            print(Ceviri)
            Not(Ceviri,Normal,dil[2])
            
            if(len(Ceviri)>200):
                Ceviri = Ceviri[200:]
                icon.notify(f'{DilAyarlari[4]}: {Ceviri}...')
            else:
                icon.notify(f'{DilAyarlari[4]}: {Ceviri}')
            """ja/en"""
            """asyncio.run(Form(X[0],Y[0],Meal))"""

        else:
            
            Log("Yazı Bulunamadı")
    except Exception as exception:
        Log(type(exception).__name__)
    
def Cizgi():

    hdc = win32gui.GetDC(None)

    pen = win32gui.CreatePen(win32con.PS_SOLID, 3, win32api.RGB(255, 0, 0))

    win32gui.SelectObject(hdc, pen)

    

    if(xyAE[0]!=xyA[0] and xyAE[1]!=xyA[1]):

        win32gui.InvalidateRect(None, None, True)
        
        win32gui.MoveToEx(hdc, xy1[0], xy1[1])
        win32gui.LineTo(hdc, xy1[0], xyA[1])

        win32gui.MoveToEx(hdc, xy1[0], xy1[1])
        win32gui.LineTo(hdc, xyA[0], xy1[1])

        win32gui.MoveToEx(hdc, xyA[0], xy1[1])
        win32gui.LineTo(hdc, xyA[0], xyA[1])

        win32gui.MoveToEx(hdc, xy1[0], xyA[1])
        win32gui.LineTo(hdc, xyA[0], xyA[1])

        win32gui.ReleaseDC(None, hdc)

        
        

def Bsayi(sayi1,sayi2):
    Sayi=["",""]
    if (sayi1>sayi2):
        Sayi=[sayi2,sayi1]
    if(sayi1<sayi2):
        Sayi=[sayi1,sayi2]

    return Sayi

def Not(CeviriT,NormalT,Dil):
    f = open(f"{DilAyarlari[4]}("+Dil+").txt", "a",encoding='utf8')
    f.write("\n\nN: "+NormalT+" \n"+"C: "+CeviriT)
    f.close()

def Log(text):
    f = open("Log.txt", "a",encoding='utf8')
    f.write("hata: "+text+" | Tarih: "+str(datetime.datetime.now()))
    f.close()

def iconUpdate():
    icon.menu=pystray.Menu(
    pystray.MenuItem(DilAyarlari[0],on_clicked,enabled=not(enbl)),
    pystray.MenuItem(DilAyarlari[1],on_clicked,enabled=enbl),
    pystray.MenuItem(f'{DilAyarlari[2]}({Diller[int(CeviriDili[3])]})',on_clicked),
    pystray.MenuItem(DilAyarlari[3],on_clicked),
    )

def on_clicked(icon,item):
    global Durumu, Acik, enbl
    if str(item) == DilAyarlari[0]:
        Durumu="durduruluyor"
        enbl=True
        iconUpdate()
        
    elif str(item) == DilAyarlari[1]:
        Durumu="başlatılıyor"
        enbl=False
        iconUpdate()

    elif str(item) == f'{DilAyarlari[2]}({Diller[int(CeviriDili[3])]})':
        ayarlar()

    elif str(item) == DilAyarlari[3]:
        icon.stop()
        Acik=False


print("Ready")

tkr='+'
keyboard.on_release_key('ctrl',printreleaseKey,suppress=False)
keyboard.on_press_key('ctrl',printPressedKey,suppress=False)






icon = pystray.Icon("",image)

iconUpdate()

icon.run()

while Acik:
    keyboard.wait()

    

