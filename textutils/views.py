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
    numberremover=(request.POST.get('numberremover','off'))
    
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
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
    
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremover!='on' and numberremover!='on'):
        return HttpResponse('please select any operation and try again!')

    return render(request, 'analyze.html', params)
