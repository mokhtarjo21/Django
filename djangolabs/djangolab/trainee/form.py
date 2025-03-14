from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import Course
from trainee.models import Trainee
class Traineeadd(forms.ModelForm):
    
    name=forms.CharField(
        label='Full Name',
        required=True,min_length=3,max_length=10,
    )
    email=forms.EmailField(label='Email')
    image=forms.ImageField(label='Profile Image')
    
    trak=forms.ModelChoiceField(queryset= (Course.objects.all()),
    label='Track')
    
    # trak=forms.ChoiceField(widget=forms.SelectMultiple,
    #     choices=[(track.id,track.name) for track in Course.objects.all()],label='Track')
    class Meta:
        model=Trainee
        fields=['name','email','image','trak']