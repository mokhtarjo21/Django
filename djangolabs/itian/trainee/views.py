from django.shortcuts import render, redirect
from .models import Trainee
def index(request):
     return render(request, 'login.html')

def add(request):
    if request.method == 'POST':
        Trainee.add_trainee(
            request.POST['name'],
            request.POST['email'],
            request.FILES['image'],
            request.POST['trak']
        )
        return redirect('/trainee')
    else:
        return render(request, 'trainee/add.html')
   

def delete(request,id):
    Trainee.objects.filter(id=id).update(isactive=False)
    return redirect('/trainee')
    

def update(request,id):
    if request.method == 'POST':
        Trainee.update_trainee(
            id,
            request.POST['name'],
            request.POST['email'],
            # request.FILES['image'],
            request.POST['trak']
        )
        return redirect('/trainee')
    else:
        context={'obj':Trainee.objects.get(id=id)}
        return render(request, 'trainee/update.html', context)

def listt(request): 
    context={}
   
    context['trainees']=Trainee.objects.filter(isactive=True)
  
    return render(request, 'trainee/listtrainee.html', context)
