from .forms import UserRegisterForm
from .forms import UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


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
                if user is not None:
                    login(request, user)
                    messages.info(request, 'Użytkownik utworzony i zalogowany')
                    return redirect('home')
            except:
                messages.error(request, 'Użytkownik utworzony ale nie można było się zalogować')
                return redirect('login_user')
    context={'form':form}
    return render(request, 'users/register.html', context)

def loginView(request):
    form= UserAuthenticationForm()
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()                 
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Zła nazwa użytkownika lub hasło')
    context={'form':form}
    return render(request, "users/login.html", context)

