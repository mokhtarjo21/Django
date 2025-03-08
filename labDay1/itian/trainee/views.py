from django.shortcuts import render, redirect
trinne=[[1,'okf'],[2,'safds']]
def index(request):
     return render(request, 'login.html')

def add(request,name):
    val=[len(trinne)+1,name]
    trinne.append(val)
    
    return redirect('/trainee')
   

def delete(request,id):
    trinne.pop(id-1)
    for i in range(len(trinne)):
        trinne[i][0]=i+1
    return redirect('/trainee')
    

def update(request):
    return render(request, 'trainee/listtrainee.html', context)

def listt(request): 
    context = {'trinne': trinne}
    return render(request, 'trainee/listtrainee.html', context)
