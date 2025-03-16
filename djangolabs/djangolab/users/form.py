# from curses.textpad import Textbox
# from django import forms
# from django.forms import TextInput
# from .models import *
# class Useradd(forms.ModelForm):
#     name=forms.CharField(
#         label='Full Name',
#         required=True,min_length=3,max_length=10,
#     )
#     email=forms.EmailField(label='Email')
#     image=forms.ImageField(label='Profile Image')
#     class Meta:
#         model=User
#         fields=['name','email','image']

# class SigninForm(forms.ModelForm):
#     class Meta:
#         model=Usernative
#         fields=['username','password']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput


class Useradd(UserCreationForm):
    age=forms.IntegerField(required=True)


from .models import *
class SigninForm(forms.ModelForm):
    class Meta:
        model=Usernative
        fields=['username','password']

class SignupForm(forms.ModelForm):
    password2=forms.CharField(required=True,widget=PasswordInput())
    class Meta:
        model=Usernative
        fields='__all__'