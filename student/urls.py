from django.urls import path
from .views import index, incomplete_student, register_class, registered_classes, mark_attendance, mark_attendance_record, find_course, err404

app_name = 'student'

urlpatterns = [
  path('', index, name='home'),
  
  path('incomplete', incomplete_student, name='incomplete_student'),
  
  path('register/classes', registered_classes, name='registered_classes'),
  
  path('register/class/new', register_class, name='register_class'),
  
  path('mark/attendance', mark_attendance, name='mark_attendance'),
  
  path('mark/attendance/course/<int:id>', find_course, name='goto_course'),
  
  path('mark/attendance/record', mark_attendance_record, name='mark_attendance_record'),
  
  path('page/not/found', err404, name='404')
]