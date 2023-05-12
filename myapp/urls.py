from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('price/',views.price,name='price'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('doctor-index/',views.doctor_index,name='doctor-index'),
    path('doctor-about/',views.doctor_about,name='doctor-about'),
    path('doctor-appointment/',views.doctor_appointment,name='doctor-appointment'),
    path('doctor-profile/',views.doctor_profile,name='doctor-profile'),
    path('book-appointment/<int:pk>/',views.book_appointment,name='book-appointment'),
    path('patient-appointment/',views.patient_appointment,name='patient-appointment'),
    path('patient-cancle-appointment/<int:pk>',views.patient_cancle_appointment,name='patient-cancle-appointment'),
    path('doctor-attend-appointment/<int:pk>/',views.doctor_attend_appointment,name='doctor-attend-appointment'),
    path('doctor-pending-appointment/',views.doctor_pending_appointment,name='doctor-pending-appointment'),
    path('doctor-attended-appointment/',views.doctor_attended_appointment,name='doctor-attended-appointment'),
    path('doctor-cancelled-appointment/',views.doctor_cancelled_appointment,name='doctor-cancelled-appointment'),
    path('patient-view-prescription/<int:pk>',views.patient_view_prescription,name='patient-view-prescription'),
]                   