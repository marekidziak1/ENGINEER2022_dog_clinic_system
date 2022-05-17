from .forms import UserRegisterForm
from .forms import UserAuthenticationForm, ProfileRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def registerUser(request):
    if not request.user.is_authenticated:
        userForm = UserRegisterForm()
        profileRegisterForm = ProfileRegisterForm()
        if request.method == 'POST':
            userForm = UserRegisterForm(request.POST)
            profileRegisterForm = ProfileRegisterForm(request.POST) #needed for checking typed data in next line (if profileRegisterForm.is_valid()) 
            if userForm.is_valid() and profileRegisterForm.is_valid():
                #Save User & create profile by signals
                user = userForm.save(commit=False)
                user.username = user.username.lower()
                user.save()
                #update Profile 
                profileRegisterForm = ProfileRegisterForm(request.POST, instance=user.profile)  
                profileRegisterForm.save()
                #Log In
                try:
                    username = userForm.cleaned_data.get('username')
                    password = userForm.cleaned_data.get('password1')
                    user = authenticate(request, username=username, password = password)
                    if user is not None:
                        login(request, user)
                        messages.info(request, 'Użytkownik utworzony i zalogowany')
                        return redirect('update_profile')
                except:
                    messages.error(request, 'Użytkownik utworzony ale nie można było się zalogować')
                    return redirect('login_user')
        context={'userForm':userForm, 'profileRegisterForm': profileRegisterForm}
        return render(request, 'users/register.html', context)
    else:
        return redirect('update_profile')

def loginUser(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect('home')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def updateProfile(request,):
    userUpdateForm = UserUpdateForm(instance=request.user)
    profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        userUpdateForm = UserUpdateForm(request.POST, instance=request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, instance=request.user.profile) #needed for checking typed data in next line (if profileRegisterForm.is_valid()) 
        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            user = userUpdateForm.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profileUpdateForm.save()
            messages.success(request, f'Your account has been updated')
            return redirect('update_profile')
        messages.error(request, f"Your account coudn't be updated")
    context={'userUpdateForm':userUpdateForm, 'profileUpdateForm': profileUpdateForm}
    return render(request, 'users/account_edit.html', context)
