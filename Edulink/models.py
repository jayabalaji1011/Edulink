from django.db import models
import datetime
import os
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def getFilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
    



class Sign_Up(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if not self.password.startswith('pbkdf2_sha256$'):  # Prevent re-hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.user_type}"

class Staff(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    MARRIED_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
    ]
    POSITION_CHOICES = [
        ('class teacher', 'Class Teacher'),
        ('subject teacher', 'Subject Teacher'),
    ]

    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_no = models.CharField(max_length=12)
    blood_group = models.CharField(max_length=5)
    DoB = models.DateField()
    subject = models.CharField(max_length=10,default='General')
    father_name = models.CharField(max_length=50)
    father_phone = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=6)
    married_status = models.CharField(max_length=7, choices=MARRIED_STATUS_CHOICES)
    position = models.CharField(max_length=15, blank=True, null=True,choices=POSITION_CHOICES)
    qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to='staff_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"



class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5)
    DoB = models.DateField()
    standard = models.IntegerField()
    section = models.CharField(max_length=1)
    father_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=15)
    mother_occupation = models.CharField(max_length=15)
    mother_name = models.CharField(max_length=50)
    mother_phone = models.CharField(max_length=12)
    register_no = models.CharField(max_length=10)
    father_phone = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=6)
    image = models.ImageField(upload_to='student_images/',null=True, blank=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"



class Assignment(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Use ForeignKey instead

    def __str__(self):
        return self.title