import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# resim dosyasını oku
image = cv2.imread('test_image.png')

# OCR işlemini gerçekleştir
text = pytesseract.image_to_string(image,lang="eng")

# metinleri tarayan dizide döngü yap
for i, t in enumerate(text):
    # metinlerin koordinatlarını al
    [x, y, w, h] = t['boundingBox']
    # resimdeki metinlerin olduğu alanları kes
    cropped_image = image[y:y + h, x:x + w]