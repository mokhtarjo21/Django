from django.urls import path, include
from course.api.views import *

from rest_framework import routers



urlpatterns=[
    
  path('update/<int:id>', update ,name='update'),
  #path('',TraineeList_add.as_view(),name='trainee_list'),
]