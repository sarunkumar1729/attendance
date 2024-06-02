from django.db import models
from django.contrib.auth.models import User


class department(models.Model):
      title=models.CharField(max_length=255)

class employee_profile(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      employee_id=models.IntegerField()
      profile_photo=models.ImageField(upload_to="images/")
      gender=models.CharField(max_length=255)
      age=models.IntegerField()
      address=models.CharField(max_length=255)
      phone=models.CharField(max_length=10)
      email=models.EmailField()
      department=models.ForeignKey(department,on_delete=models.CASCADE)
      joining_date=models.DateField()
      starting_salary=models.IntegerField()
      current_salary=models.IntegerField()

class leave_requests(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      date=models.DateField()
      message=models.TextField(max_length=255)
      status=models.CharField(max_length=255,default='pending')

class attendance(models.Model):
      date=models.DateField(auto_now=True)
      user=models.ForeignKey(employee_profile,on_delete=models.CASCADE)
      status=models.CharField(max_length=255)
