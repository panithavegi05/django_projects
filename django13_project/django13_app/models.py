
from django.db import models # type: ignore
class Student(models.Model): 
    name = models.CharField(max_length=100) 
    age = models.IntegerField() 
    email = models.EmailField()