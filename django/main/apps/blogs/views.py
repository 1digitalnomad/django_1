from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = " placeholder to later display all the list of blogs"
    return HttpResponse(response)
# Create your views here.

def test(request):
    response = "Hello I am test!"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse("placeholder to display blog " + number)

def edit(request, num):
    print(num)
    return HttpResponse("placeholder to edit blog " + num)

def destroy(request, num):
    return redirect('/')