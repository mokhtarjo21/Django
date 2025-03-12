from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
 @classmethod
    def get_all_course(cls):
        return cls.objects.all()
    @classmethod
    def get_course_by_id(cls,id):
        return cls.objects.get(id=id)
    @staticmethod
    def add_course(name,description,price):
        return Course.objects.create(name=name,description=description,price=price)
    @classmethod
    def update_course(cls,id,name,email,image,trak):
        return cls.objects.filter(id=id).update(name=name,description=description,price=price)
   

