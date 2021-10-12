from datetime import timezone
from attendance.funcs import setTimeOut
from auth_users.models import Profile
from django.contrib.auth.models import User
from .models import Attendance, Course
from django.test import TestCase

# Create your tests here.
class Test(TestCase):
  
  
  def setUp(self):
    u = User.objects.create(username='STAFF12345', password='12345678').save()
    
    course = Course.objects.create(name='Java', code='Comp200')
    course.save()
    

  # def test_course_created(self):
  #   course = Course.objects.get(code='Comp200')
    
  #   self.assertEqual(course is not None, True)

  # def test_course_to_lecture_created(self):
  #   profile = Profile.objects.get(user__username='STAFF12345')
  #   course = Course.objects.get(code='Comp200')
  #   profile.lecturer.courses.add(course)
  #   profile.save()
  #   print(profile.lecturer.courses.all())
  #   self.assertEqual(profile.lecturer.courses is not None, True)
    
    
def test_attendance(self):
  attendance = Attendance(time_limit=setTimeOut(minutes=-10))
  attendance.save()
  print(attendance.time_limit)
  self.assertEqual( attendance.time_limit == timezone.now(), True )
    