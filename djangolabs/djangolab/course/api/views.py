from django.template.context_processors import request

from .serlizer import C_serlizer
from rest_framework import generics
from course.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

def update(request,id):
    Course1=get_object_or_404(Course,id=id)
    if request.method=='put':
        objserlized=C_serlizer(data=request.data,instance=Course1)
      
        if(objserlized.is_valid()):
            objserlized.save()
            return Response(
            data=objserlized.data,
            status=status.HTTP_200_OK)
        else:
         return Response(data=
                         {
                            'errors':objserlized.errors
                         })
    return Response(data=
                    {
                        'errors':'invalid request'
                    })