from django.shortcuts import render,redirect
from .models import User,Doctor,Appointment

# Create your views here.
def index(request):
	doctors=Doctor.objects.all()
	return render(request,'index.html',{'doctors':doctors})

def doctor_index(request):
	return render(request,'doctor-index.html')

def doctor_appointment(request):
	user=User.objects.get(email=request.session["email"])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
	request.session['appointment_count']=len(appointments)
	return render(request,'doctor-appointments.html',{'appointments':appointments})

def doctor_pending_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
	
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def doctor_cancelled_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Cancelled")
	
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def doctor_attended_appointment(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor.objects.get(doctor=user)
	appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Attended")
	
	return render(request,'doctor-appointment.html',{'appointments':appointments})

def patient_view_prescription(request,pk):
	appointment=Appointment.objects.get(pk=pk)
	return render(request,'patient-view-prescription.html',{'appointment':appointment})



def doctor_profile(request):
	user=User.objects.get(email=request.session['email'])
	doctor=Doctor()
	try:
		doctor=Doctor.objects.get(doctor=user)
	except:
		pass 
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.clinic_address=request.POST['clinic_address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		doctor.doctor=user 
		doctor.clinic_address=request.POST['clinic_address']
		doctor.qualification=request.POST['qualification']
		doctor.speciality=request.POST['speciality']
		doctor.save()
		msg="Profile Updated Successfully"
		return render(request,'doctor-profile.html',{'user':user,'doctor': doctor,'msg':msg})

	else:
		return render(request,'doctor-profile.html',{'user':user,'doctor': doctor})

def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')

def doctor_about(request):
	user=User.objects.get(email=request.session["email"])
	doctor=Doctor.objects.get(doctor=user)
	return render(request,'doctor-about.html',{'doctor':doctor})

def service(request):
	return render(request,'service.html')

def price(request):
	return render(request,'price.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST["email"])
			msg="email already exists"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					usertype=request.POST['usertype'],
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					)
				msg="User signup sucessfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm Password does not matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
 	if request.method=="POST":
 		try:
 			user=User.objects.get(email=request.POST['email'])
 			if user.password==request.POST['password']:
	 			if user.usertype=='patient':
		 			request.session['email']=user.email
		 			request.session['fname']=user.fname 
		 			request.session['profile_pic']=user.profile_pic.url				
		 			return redirect('index')		 				
		 		else:
		 			
		 			doctor=Doctor.objects.get(doctor=user)
		 			appointments=Appointment.objects.filter(doctor=doctor,appointment_status="Pending")
		 			request.session['email']=user.email
		 			request.session['fname']=user.fname 
		 			request.session['profile_pic']=user.profile_pic.url
		 			request.session['appointment_count']=len(appointments)				
		 			return render(request,'doctor-index.html')		 			
 			else:
 				msg="incorrect password"
 				return render(request,'login.html',{'msg':msg})
 		except:
 			msg="Email not registered"
 			return render(request,'login.html',{'msg':msg})
 	else:
 		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def book_appointment(request,pk):
	doctor=Doctor.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Appointment.objects.create(
				doctor=doctor,
				user=user,
				date=request.POST['date'],
				time=request.POST['time'],
				health_issue=request.POST['health_issue'],

			)
		msg="appointment Booked Successfully"
		return render(request,'appointment.html',{'doctor':doctor,'user':user,'msg':msg})
	else:
		return render(request,'appointment.html',{'doctor':doctor,'user':user})

def patient_appointment(request):
	user=User.objects.get(email=request.session['email'])
	appointments=Appointment.objects.filter(user=user)
	return render(request,'patient-appointment.html',{'appointments':appointments})

def patient_cancle_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk )
	if request.method=="POST":
		appointment.cancle_reason=request.POST['cancle_reason']
		appointment.appointment_status="Cancelled"
		appointment.save()
		msg="Appointment cancelled successfully"
		return render(request,'patient-cancle-appointment.html',{'appointment':appointment,'msg':msg})

	else:
		return render(request,'patient-cancle-appointment.html',{'appointment':appointment})

def doctor_attend_appointment(request,pk):
	appointment=Appointment.objects.get(pk=pk )
	if request.method=="POST":
		appointment.prescription=request.POST['prescription']
		appointment.appointment_status="Attended"
		appointment.save()
		msg="Appointment Attended Successfully"
		return redirect('doctor-appointment')

	else:
		return render(request,'doctor-attend-appointment.html',{'appointment':appointment})
