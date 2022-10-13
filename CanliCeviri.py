import re
import pytesseract 
from PIL import Image, ImageGrab
from googletrans import Translator
import numpy as np
import cv2 
translator=Translator()

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
while True:
    img= ImageGrab.grab(bbox=(300,790,1900,950))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

    
    cv2.imshow('Ekran',img_final)

    if cv2.waitKey(1)==ord('ç'):
        b = pytesseract.image_to_string(img_final,lang ='jpn')
        a = re.sub(r'\n', ' ', b)
        print("\n\n\n\n"+translator.translate(a,src='ja',dest='tr').text)
        print("\n"+a)
        
    
    if cv2.waitKey(10)==ord('q'):
        cv2.destroyAllWindows()
        break

