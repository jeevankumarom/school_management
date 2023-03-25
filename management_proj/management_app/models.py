from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class school(models.Model):
    school_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    address=models.TextField()
    mail=models.EmailField()
    phone_number=models.CharField(max_length=13)
    created_date=models.DateField(auto_now=datetime.datetime.now())


class classes(models.Model):
    class_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    school = models.ForeignKey(school, on_delete=models.CASCADE)

class section(models.Model):
    section_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    
class subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    school = models.ForeignKey(school,on_delete=models.CASCADE)
    
class students(models.Model):
    student_id=models.CharField(max_length=150,primary_key=True)
    school = models.ForeignKey(school,on_delete=models.CASCADE)
    section=models.ForeignKey(section,on_delete=models.CASCADE)
    classes=models.ForeignKey(classes,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    address=models.TextField()
    dob=models.DateField()
    phone_number=models.CharField(max_length=13)
    email=models.EmailField()
    joining_date=models.DateField(auto_now=datetime.datetime.now())


class staffs(models.Model):
    staff_id=models.CharField(max_length=150,primary_key=True)
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    classes=models.CharField(max_length=250)
    section=models.CharField(max_length=250)
    name=models.CharField(max_length=120)
    role=models.CharField(max_length=250)
    age=models.IntegerField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=13)
    joining_date=models.DateField(auto_now=datetime.datetime.now())

class marks(models.Model):
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    student=models.ForeignKey(students,on_delete=models.CASCADE)
    mark=models.BigIntegerField()

class login_info(models.Model):
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    student=models.ForeignKey(students,on_delete=models.CASCADE,null=True,blank=True)
    staff=models.ForeignKey(staffs,on_delete=models.CASCADE,null=True,blank=True)
    user_name=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
