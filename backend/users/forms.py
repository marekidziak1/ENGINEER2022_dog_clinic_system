from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'g__form-input input'})
        self.fields['email'].widget.attrs.update({'class': 'g__form-input input'})
        self.fields['password1'].widget.attrs.update({'class': 'g__form-input input'})
        self.fields['password2'].widget.attrs.update({'class': 'g__form-input input'})