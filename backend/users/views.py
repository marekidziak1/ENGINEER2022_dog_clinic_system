from codecs import utf_16_be_decode
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def registerView(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            #logowanie
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password = password)
            except:
                messages.error(request, 'Użytkownik utworzony ale nie można się zalogować')
                return redirect('login_user')
            if user is not None:
                login(request, user)
                return redirect('home')
    context={'form':form}
    return render(request, 'users/register.html', context)

def loginView(request):
    context={}
    return render(request,"users/login.html" ,context)