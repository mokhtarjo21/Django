from django.urls import path ,include
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    # path('add/', views.add ,name= 'add'),
    # path('delete/<int:id>', views.delete ,name= 'delete'),
    # path('update/<int:id>', views.update ,name= 'update'),
    path('api/' ,include('course.api.url')),
    ]