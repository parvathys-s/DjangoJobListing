from django.db import models
# Create your models here.

class Job(models.Model):
    companyname = models.CharField(max_length=50)
    jobrole = models.CharField(max_length=50)
    salary = models.IntegerField()
    dateposted = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)

