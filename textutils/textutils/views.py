# File created by Sahaj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1>Home</h1>")
    params={'Name':'Sahaj','Place':'Mars'}
    return render(request, 'index.html', params)

def removePunc(request):
    return HttpResponse("Remove Punctuation")
def capFirst(request):
    return HttpResponse("Capitalize First")
def newLineRemove(request):
    return HttpResponse("new line removal")
def spaceRemove(request):
    return HttpResponse("space remove")
def charCount(request):
    return HttpResponse("Character Counter")