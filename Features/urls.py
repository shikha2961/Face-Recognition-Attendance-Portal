from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('attendance/',views.attendance_recognition,name="attendance_recognition"),
    path('View_Att/', views.view_attendance, name='view_attendance'),
    path('admin/', views.adminpage, name='adminpage')
]
