from django.shortcuts import render , redirect
from .models import Course
from .form import courseaddmodel
def index(request):
    context={'courses':Course.get_all_course()}
    return render(request, 'course/course.html', context)

def add(request):
    context={'form':courseaddmodel()}
    
    if(request.method=='POST' ):
        form=courseaddmodel(data=request.POST,files=request.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            
            return redirect('/course')
        else:
            context['error']=form.errors
            return render(request, 'course/addcourse.html', context)
    return render(request,'course/addcourse.html',context)

def update(request):
    return render(request, 'course/course.html', context)

def delete(request,id):
    Course.get_course_by_id(id).delete()
    return redirect('/course')
