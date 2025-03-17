from django.urls import path, include
from .views import *
from .views import *
from rest_framework import routers



urlpatterns=[
    
  path('',TraineeList_add.as_view(),name='trainee_list'),
  path('<pk>/',trainee_update_delete.as_view(),name='trainee_update_delete'),
]