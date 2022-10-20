import keyboard
import pyautogui
import re
import pytesseract 
from PIL import Image, ImageGrab
from googletrans import Translator
import numpy as np
import cv2 
import win32gui, win32ui
import time

translator=Translator()

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def printPressedKey(e):
    global tkr,xy1,xyA,xyAE,Cs
    if(tkr=='+'):
        Cs=0
        start_time = time.time()
        xy1=pyautogui.position()
        xyA=xy1
        xyAE=xyA
        tkr='-'
    else:
        xyAE=xyA
        xyA=pyautogui.position()
    Cizgi()

def printreleaseKey(e):
    global tkr,xy2,dil
    xy2=pyautogui.position()
    tkr="+"
    try:
        win32gui.InvalidateRect(hwnd,None,True)
    except:
        print("")
    if (e.name=='alt'): 
        dil=["jpn","ja"]
    if(e.name=='ctrl'): 
        dil=["eng","en"]
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
        a = re.sub(r'\n', ' ', b)

        if(b!=""):
            print("\n"+a)
            print(translator.translate(a,src=dil[1],dest='tr').text)
            """ja/en"""
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

    
tkr='+'

keyboard.on_release_key('alt',printreleaseKey,suppress=False)
keyboard.on_release_key('ctrl',printreleaseKey,suppress=False)

keyboard.on_press_key('alt',printPressedKey,suppress=False)
keyboard.on_press_key('ctrl',printPressedKey,suppress=False)
while True:
    keyboard.wait('esc')
