from django.shortcuts import render, redirect
from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import Course
from .models import Trainee
from .form import Traineeadd
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
import os
from django.conf import settings
from django.views.generic import UpdateView,DeleteView
from django.views import View

class add(View):
    @login_required
    def get(self,request):
        context={'form':Traineeadd()}
        return render(request, 'trainee/add.html', context)
    @login_required
    def post(self,request):
        form=Traineeadd(data=request.POST,files=request.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('/trainee')
        else:
            context['error']=form.errors
            return render(request, 'trainee/add.html', context)

class delete(DeleteView):
    def get(self,request,id):
        Trainee.objects.filter(id=id).update(isactive=False)
        return redirect('/trainee')
  
class update(UpdateView):
    def get(self,request,id):
        obj=Trainee.get_trainee_by_id(id)

        course=Course.get_all_course()
        context={'obj':obj,'courses':course}
        return render(request, 'trainee/update.html', context)
    def post(self,request,id):
        obj=Trainee.get_trainee_by_id(id)
        if obj.image:
            old_image_path ='media/trainee/'+str(obj.image)
            print(os.path.exists(old_image_path))
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
                print('removed')
        obj.image=request.FILES['image']
        obj.name=request.POST['name']
        obj.email=request.POST['email']
        obj.trak=Course.get_course_by_id(request.POST['trak'])
        obj.save()
        return  redirect('/trainee')
class listt(View):
    def get(self,request):
        context={}
        context['trainees']=Trainee.objects.filter(isactive=True)
        return render(request, 'trainee/listtrainee.html', context)    
def index(request):
     return render(request, 'login.html')

# def add(request):
#     context={'form':Traineeadd()}
    
#     if(request.method=='POST' ):
#         form=Traineeadd(data=request.POST,files=request.FILES)
#         if(form.is_bound and form.is_valid()):
#             form.save()
#             return redirect('/trainee')
#         else:
#             context['error']=form.errors
#             return render(request, 'trainee/add.html', context)
#     return render(request, 'trainee/add.html', context)
   

# def delete(request,id):
#     Trainee.objects.filter(id=id).update(isactive=False)
#     return redirect('/trainee')
    

# def update(request,id):
#     obj=Trainee.get_trainee_by_id(id)

#     course=Course.get_all_course()
#     context={'obj':obj,'courses':course}
#     if(request.method=='POST'):
#         if obj.image:
#             old_image_path ='media/trainee/'+str(obj.image)
#             print(os.path.exists(old_image_path))
#             if os.path.exists(old_image_path):
#                 os.remove(old_image_path)
#                 print('removed')
#         obj.image=request.FILES['image']
#         obj.name=request.POST['name']
#         obj.email=request.POST['email']
#         obj.trak=Course.get_course_by_id(request.POST['trak'])
#         obj.save()
#         return  redirect('/trainee')
#     else:

#         return render(request, 'trainee/update.html', context)

# def listt(request): 
#     context={}
   
#     context['trainees']=Trainee.objects.filter(isactive=True)
  
#     return render(request, 'trainee/listtrainee.html', context)
