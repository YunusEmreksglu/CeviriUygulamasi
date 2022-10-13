import keyboard
import pyautogui

import re
import pytesseract 
from PIL import Image, ImageGrab
from googletrans import Translator
import numpy as np
import cv2 

translator=Translator()

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def printPressedKey(e):
    global tkr,xy1
    if(tkr=='+'):
        xy1=pyautogui.position()
        tkr='-'
    
    
def printreleaseKey(e):
    global tkr,xy2
    xy2=pyautogui.position()
    tkr="+"
    
    img= ImageGrab.grab(bbox=(xy1[0],xy1[1],xy2[0],xy2[1]))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)  

    b = pytesseract.image_to_string(img_final,lang ='jpn')
    a = re.sub(r'\n', ' ', b)

    if(b!=""):
        print("\n"+a)
        
        print(translator.translate(a,src='ja',dest='tr').text)
    else:
        print("Yazı Bulunamadı")
 
tkr='+'

keyboard.on_release_key('alt',printreleaseKey,suppress=False)
keyboard.on_press_key('alt',printPressedKey,suppress=False)

while True:
    keyboard.wait('')
