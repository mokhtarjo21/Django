from rest_framework import serializers
from course.models import Course
from django.shortcuts import get_object_or_404,get_list_or_404

class C_serlizer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
    
    @classmethod
    def get_all_course(cls):
        return  cls(Course.get_all_course,many=True).data

    @classmethod
    def get_course_by_id(cls,id):

        return cls(get_object_or_404(Course,id=id)).data
