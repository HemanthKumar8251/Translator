from googletrans import Translator

translator = Translator()
text = 'hello how are you'
sr = 'en'
de = 'fr'
translated = translator.translate(text, src= sr, dest =  de)
result = translated.text

print(result)