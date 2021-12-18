# i created this file - Mohammed Safwan
from django.http import HttpResponse, response
from django.shortcuts import render


def index(request):
    return render(request,'index.html')



def analyze(request):
    #get the text
    djtext=(request.POST.get('text','default'))
    # check checbox value on/off
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    spaceremover=(request.POST.get('spaceremover','off'))
    
    if removepunc=='on':
        analyzed=""
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps=='on':
        analyzed=""
        analyzed=djtext.upper()
        params={'purpose':'Capitalized','analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover=='on':
        analyzed=""
        djtext = djtext.replace('\r\n',' ').replace('\n','')
        for char in djtext:
            #  and char!='\r'
            if char!='\n':
                analyzed=analyzed+char
        params={'purpose':'Removed new line','analyzed_text':analyzed}
        djtext=analyzed

    if spaceremover=='on':
        analyzed=""
        try:
            for index,char in enumerate(djtext):
                if not (djtext[index]==" " and djtext[index+1]==" "):
                    analyzed=analyzed+char
        except Exception as e:
            print(e)
        params={'purpose':'Removed Spaces','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremover!='on'):
        return HttpResponse('please select any operation and try again!')

    return render(request, 'analyze.html', params)

    











# def cap(request):
#     return HttpResponse('<h1>capitalize</h1><a href="/" style="border: 1px solid black; border-radius: 10px; padding: 5px">back</a>')

# def newlineremove(request):
#     return HttpResponse('<h1>newlineremove</h1><a href="/" style="border: 1px solid black; border-radius: 10px; padding: 5px">back</a>')

# def spaceremover(request):
#     return HttpResponse('<h1>spaceremover</h1><a href="/" style="border: 1px solid black; border-radius: 10px; padding: 5px">back</a>')

# def charcount(request):
#     return HttpResponse('<h1>charcount</h1><a href="/" style="border: 1px solid black; border-radius: 10px; padding: 5px">back</a>')