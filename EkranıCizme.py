import win32api
import win32gui

#Pega o contexto gráfico para o Desktop
dc = win32gui.GetDC(0)
while True:
    win32gui.MoveToEx(dc,0,0)
    win32gui.LineTo(dc,1366,768)
    