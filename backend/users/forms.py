from .models import Profile
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=TextInput(attrs={'class': 'g__form-input input','placeholder': 'username','type':"text"}))
    password1 = forms.CharField(max_length=30, widget=PasswordInput(attrs={'class': 'g__form-input input','placeholder':'type password','type':"password"}))
    password2 = forms.CharField(max_length=30,widget=PasswordInput(attrs={'class': 'g__form-input input','placeholder':'confirm password','type':"password"}))
    class Meta:
        model=User
        fields = ['username','password1','password2']
    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'g__form-input input', 'type':"text"})
    #     self.fields['password1'].widget.attrs.update({'class': 'g__form-input input', 'type':"password"})
    #     self.fields['password2'].widget.attrs.update({'class': 'g__form-input input', 'type':"password"})

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=20, widget=TextInput(attrs={'class': 'g__form-input input','placeholder': 'username','type':"text"}))
    password = forms.CharField(max_length=30, widget=PasswordInput(attrs={'class': 'g__form-input input','placeholder':'password','type':"password"}))
    class Meta:
        model = User
        fields = ['username','password']

class ProfileRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=60, widget=TextInput(attrs={'class': 'g__form-input input','placeholder': 'name & surname','type':"text"}))
    mobileNumber = PhoneNumberField(widget=TextInput(attrs={'class': 'g__form-input input','placeholder': 'phone number','type':"text"}))#(max_length=15, widget=TextInput(attrs={'class': 'g__form-input input','placeholder': 'username','type':"text"}))
    class Meta:
        model = Profile
        fields = ['name','mobileNumber']