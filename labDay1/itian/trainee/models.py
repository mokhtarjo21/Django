from django.db import models

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='trainee/images/')
    isactive=models.BooleanField(default=True)
# Create your models here.
