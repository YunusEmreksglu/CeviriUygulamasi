from  googletrans import Translator
translator = Translator()
text='World'

a = translator.translate(text,src='ja',dest='tr')

print(a.text)
