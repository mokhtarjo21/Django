from django.db import models
from course.models import Course
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='trainee/images/')
    isactive=models.BooleanField(default=True)
    trak=models.ForeignKey(to=Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    @classmethod
    def get_all_trainee(cls):
        return cls.objects.all()
    @classmethod
    def get_trainee_by_id(cls,id):
        return cls.objects.get(id=id)
    @staticmethod
    def add_trainee(name,email,image,trak):
        return Trainee.objects.create(name=name,email=email,image=image,trak=Course.get_course_by_id(trak))
    @classmethod
    def update_trainee(cls,id,name,email,image,trak):
        return cls.objects.filter(id=id).update(name=name,email=email,trak=trak)
    @classmethod
    def get_trainee_by_active(cls):
        return cls.objects.filter(isactive=True)

