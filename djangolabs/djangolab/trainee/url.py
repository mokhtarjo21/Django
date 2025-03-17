from django.urls import path , include
from .views import *
from django.views import View
from django.contrib.auth.decorators import login_required
from users.views import *
from django.contrib.auth import authenticate,login,logout

urlpatterns = [
 
    path('', login_required(listt.as_view())  ,name= 'listt'),
    path('add/', login_required(add.as_view()),name= 'add'),
    path('delete/<int:id>', login_required(delete.as_view()) ,name= 'delete'),
    path('update/<int:id>', login_required(update.as_view()) ,name= 'update'),
    path('api/',include('trainee.api.url')),
]