from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return render(request, 'about.html', {'gretting':'hello'})
    a = 5+6
    return render(request, 'about.html', {'gretting':a})

def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request, 'reverse.html',{'word':reverse})

def home(request):
    return HttpResponse('This is my first home')