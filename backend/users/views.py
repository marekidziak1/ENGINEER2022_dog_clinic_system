from django.shortcuts import render

# Create your views here.
def registerView(request):
    context={}
    return render(request,"users/register.html" ,context)
def loginView(request):
    context={}
    return render(request,"users/login.html" ,context)