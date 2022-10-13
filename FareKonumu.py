import keyboard
import pyautogui
 
def printPressedKey(e):
    global tkr,xy1
    if(tkr=='+'):
        for i in range(5, 0, -1):
            pyautogui.moveTo(100, 100, duration=0.10*i)
            pyautogui.moveTo(200, 100, duration=0.10*i)
            pyautogui.moveTo(200, 200, duration=0.10*i)
            pyautogui.moveTo(100, 200, duration=0.10*i)
        print("bastın")
        xy1=pyautogui.position()
        tkr='-'
    
    
def printreleaseKey(e):
    global tkr,xy2
    print("kaldırdın")
    xy2=pyautogui.position()
    tkr="+"
    print(str(xy1[0])+" "+str(xy1[1])+" "+str(xy2[0])+" "+str(xy2[1])+" ")
 
tkr='+'
keyboard.on_release_key('e',printreleaseKey,suppress=False)
keyboard.on_press_key('e',printPressedKey,suppress=False)
 
while True:
    keyboard.wait('win')
