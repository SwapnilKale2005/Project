from django.db import models


class Course(models.Model):
    branch = models.CharField(max_length=10)
    year = models.IntegerField(max_length=3)
    pt = models.CharField(max_length=3)
    question1 = models.CharField(max_length=4)
    question2 = models.CharField(max_length=4)
    question3 = models.CharField(max_length=4)
    question4 = models.CharField(max_length=4)
    question5 = models.CharField(max_length=4)
    question6 = models.CharField(max_length=4)
    question7 = models.CharField(max_length=4)
    question8 = models.CharField(max_length=4)
    class Meta:
        abstract=True

class Marks(models.Model):
    roll_no = models.IntegerField(primary_key=True) 
    branch = models.CharField(max_length=10)
    year = models.IntegerField()         
    pt = models.CharField(max_length=3) 
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    # Create your models here.
    class Meta:
        abstract=True

