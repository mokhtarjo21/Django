from django.template.context_processors import request

from .serlizer import T_serlizer
from rest_framework import generics
from ..models import Trainee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class TraineeList_add(APIView):
    def get(self, request):
        trainee = Trainee.objects.all()
        serlizer = T_serlizer(trainee, many=True)
        return Response(serlizer.data)

    def post(self, request):
        serlizer = T_serlizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response(serlizer.data, status=status.HTTP_201_CREATED)
        return Response(serlizer.errors, status=status.HTTP_400_BAD_REQUEST)

class trainee_update_delete(generics.RetrieveAPIView):
    queryset = Trainee.get_trainee_by_active()
    serializer_class = T_serlizer
    