from django.shortcuts import render , redirect
courses = [[1,'python'],[2,'java'],[3,'c++'],[4,'c#'],[5,'php']]
def index(request):
    context = {
        'courses': courses
    }
    return render(request, 'course/course.html', context)

def add(request,name):
    val=[len(courses)+1,name]
    courses.append(val)
    
    return redirect('/course')
   
def update(request):
    return render(request, 'course/course.html', context)

def delete(request,id):
    courses.pop(id-1)
    for i in range(len(courses)):
        courses[i][0]=i+1
    return redirect('/course')
    
# Create your views here.
