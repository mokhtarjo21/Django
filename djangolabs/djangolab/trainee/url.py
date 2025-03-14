from django.urls import path
from .views import *
from django.views import View

urlpatterns = [
 
    path('add/', add.as_view() ,name= 'add'),
    path('delete/<int:id>', delete.as_view() ,name= 'delete'),
    path('update/<int:id>', update.as_view()  ,name= 'update'),
    path('', listt.as_view()  ,name= 'listt'),
]