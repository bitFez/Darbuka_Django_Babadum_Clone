from googletrans import Translator
translator = Translator()
text = translator.translate("hello", src="en", dest="tr", )

print(text)