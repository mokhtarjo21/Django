from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import course

class courseaddmodel(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
        exclude=['id','created_at ','updated_at']
class Courseadd(forms.Form):
    
    name=forms.CharField(
        label='Full Name',
        required=True,min_length=3,max_length=10,
    )
    description=forms.CharField(label='description')
    price=forms.DecimalField(label='price')
    
    
    