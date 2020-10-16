from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    q_id = models.AutoField(primary_key=True)
    q_no = models.IntegerField(default=0)
    question = models.CharField(max_length=500)
    a1 = models.CharField(max_length=200)
    a2 = models.CharField(max_length=200)
    a3 = models.CharField(max_length=200)
    a4 = models.CharField(max_length=200)
    c = models.IntegerField()

class User_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_attempted = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

