from django.urls import path, include
from course.api.views import *
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet


router = DefaultRouter()
router.register(r'', CourseViewSet)


urlpatterns=[
    
  path('update/<int:id>', update ,name='update'),
  path('', include(router.urls)),
]