from django.shortcuts import render, redirect
from .models import Trainee
from .form import Traineeadd
def index(request):
     return render(request, 'login.html')

def add(request):
    context={'form':Traineeadd()}
    
    if(request.method=='POST' ):
        form=Traineeadd(data=request.POST,files=request.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('/trainee')
        else:
            context['error']=form.errors
            return render(request, 'trainee/add.html', context)
    return render(request, 'trainee/add.html', context)
   

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
