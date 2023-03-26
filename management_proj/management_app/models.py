from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    

class Student(CustomUser):
    student_id=models.CharField(max_length=10,primary_key=True,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cls=models.ForeignKey(classes,on_delete=models.CASCADE)
    sec=models.ForeignKey(section,on_delete=models.CASCADE)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

class Staff_register_login(CustomUser):
    staff_id=models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cls=models.ForeignKey(classes,on_delete=models.CASCADE)
    sec=models.ForeignKey(section,on_delete=models.CASCADE)
    school=models.ForeignKey(school,on_delete=models.CASCADE)
    def get_full_name(self):
        return self.first_name + " " + self.last_name