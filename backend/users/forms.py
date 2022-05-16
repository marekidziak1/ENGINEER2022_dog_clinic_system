from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'g__form-input input', 'type':"text"})
        self.fields['password1'].widget.attrs.update({'class': 'g__form-input input', 'type':"text"})
        self.fields['password2'].widget.attrs.update({'class': 'g__form-input input', 'type':"text"})