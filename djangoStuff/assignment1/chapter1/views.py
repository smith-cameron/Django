from django.shortcuts import render, HttpResponse, redirect
def home_page(request):
    return HttpResponse("Placeholder to later display list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'placeholder to display blog number:{number}' )
def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number:{number}')
def destroy(request, number):
    return redirect('/')
def index(request, name):
    context = {
        "htmlname": name
    }
    return render(request, "home.html", context)
