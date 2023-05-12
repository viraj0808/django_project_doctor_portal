from django.db import models


# Create your models here.
class User(models.Model):
	userchoice=(
		   ('patient','patient'),
		   ('doctor','doctor')
		)
	usertype=models.CharField(max_length=100,choices=userchoice)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to='profile_pic/',default="")

	def __str__(self):
		return self.fname+"  "+self.lname

class Doctor(models.Model):
	doctor=models.ForeignKey(User,on_delete=models.CASCADE)
	clinic_address=models.TextField()
	qualification=models.CharField(max_length=100)
	speciality=models.CharField(max_length=100)
	profile=models.BooleanField(default=False)
	charges=models.PositiveIntegerField(default=200)

	def __str__(self):
		return self.doctor.fname+" - "+self.speciality   

class Appointment(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	health_issue=models.TextField()
	appointment_status=models.CharField(max_length=100,default="Pending")
	cancle_reason=models.TextField(default="")
	prescription=models.TextField(default="")

	def __str__(self):
		return self.doctor.doctor.fname+" - "+self.user.fname


    		