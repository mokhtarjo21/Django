from django.shortcuts import render , redirect
from .models import Course
from .forms import Courseadd ,courseaddmodel
def index(request):
    context = {
        'courses': Course.get_all_course()
    }
    return render(request, 'course/course.html', context)

def add(request):
    if(req.method=='POST' ):
        form=courseaddmodel(data=req.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
        return redirect('/course')
    else
        context={'form':courseaddmodel()}

        render(request, 'course/addcourse.html', context)
   
def update(request):
    return render(request, 'course/course.html', context)

def delete(request,id):
    courses.pop(id-1)
    for i in range(len(courses)):
        courses[i][0]=i+1
    return redirect('/course')
    
# Create your views here.
