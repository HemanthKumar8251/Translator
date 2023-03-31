from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponse
import speech_recognition as speech  


# Create your views here.
def T2T(request):
    if(request.method == 'GET'):
        return render(request,'Translate/t2t.html')
    if(request.method == 'POST'): 
        print('post') 
        text = request.POST['text']
        print(text)
        print(type(text))
        sr = request.POST['sr']
        de = request.POST['de']
        print(sr,de)
        translator = Translator()
        translated = translator.translate(text,src= sr, dest =  de)
        result = translated.text
        print(result)
        return render(request,'Translate/t2t.html',{'result':result})

    
def S2T(request):
     if(request.method == 'GET'):
        return render(request,'Translate/s2t.html')
     if(request.method == 'POST'): 
        print('post') 
        sr = request.POST['sr']
        de = request.POST['de']
        print(sr,de)
        
        r = speech.Recognizer()
        with speech.Microphone() as s:
          print("Speak now...")
        audio = r.listen(s)
        try:
            text = r.recognize_google(audio, language=sr)

            print(f"you have said {text}")
            translator = Translator()
            translated = translator.translate(text,src= sr, dest =  de)
            result = translated.text
        except Exception as e:
            result = "Error: {str(e)}"
        return render(request, 'Translate/s2t.html', {
            'result' :result
        })
def home(request): 
    return render(request,'Translate/index.html')