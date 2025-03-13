from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import Course

class courseaddmodel(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        exclude=['id','created_at ','updated_at']
