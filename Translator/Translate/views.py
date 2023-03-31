from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponse


# Create your views here.
def T2T(request):
    return render(request,'Translate/t2t.html')
def T2TR(request):
    if(request.method == 'POST'): 
        print('post')  
        text = request.POST['text']
        print(text)
        print(type(text))
        sr = request.POST['sr']
        de = request.POST['de']
        print(sr,de)
        translator = Translator()
        translated = translator.translate(text, sr, de)
        result = translated.text
        print(result)
        return render(request,'Translate/t2tR.html',{'result':result})
    if(request.method == 'GET'):
        return HttpResponse("JHgdjhg")
def S2T(request):
    pass
def home(request): 
    return render(request,'Translate/index.html')