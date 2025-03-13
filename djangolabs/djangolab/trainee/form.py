from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import Course
from .models import Trainee

class Traineeadd(forms.Form):
   
    name=forms.CharField(
        label='Full Name',
        required=True,min_length=3,max_length=10,
    )
    email=forms.EmailField(label='Email')
    image=forms.ImageField(label='Profile Image')
    
    trak=forms.ChoiceField(widget=forms.SelectMultiple,
        choices=[(cou.id,cou.name) for cou in Course.get_all_course()]
    )
   