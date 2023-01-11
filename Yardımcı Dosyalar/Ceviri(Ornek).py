from  googletrans import Translator
translator = Translator()
text='World'

a = translator.translate(text,src='en',dest='tr')

print(a.text)
