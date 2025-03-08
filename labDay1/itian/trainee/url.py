from django.urls import path
from . import views


urlpatterns = [
    
    path('add/<str:name>', views.add ,name= 'add'),
    path('delete/<int:id>', views.delete ,name= 'delete'),
    path('update', views.update ,name= 'update'),
    path('', views.listt ,name= 'listt'),
]