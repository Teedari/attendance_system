import datetime
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.contrib.auth.models import User
from helpers.funcs import validateTimer

# Create your models here.




class MarkAttendance(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(to=User,null=True, related_name='user', on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.user} - {self.date} '
  
  
  
class Attendance(models.Model):
  id = models.AutoField(primary_key=True)
  attendances = models.ManyToManyField(to=MarkAttendance, related_name='attendances', blank=True)
  time_limit = models.CharField(blank=True, max_length=30)
  accessible = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.created_at}'
  
  @property
  def isTimeOut(self):
    return validateTimer(self.time_limit)
    
    
    
  @property
  def isOpened(self):
    return self.accessible
  
  @property
  def attendedStudents(self):
    stds = [ std.user for std in self.attendances.all() ]
    return stds
  
  @property
  def isToday(self):
    return self.created_at.date() == datetime.datetime.now().date()


class Course(models.Model):
  name = models.CharField(max_length=100)
  code = models.CharField(max_length=100, unique=True)
  qr_code = models.ImageField(blank=True, upload_to='qr_codes')
  location = models.CharField(max_length=200, blank=True)
  attendance = models.ManyToManyField(to=Attendance, related_name='attendance', blank=True)
  # attendance = models.ForeignKey(to=Attendance, related_name='attendance', on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return f'{self.name} - {self.code}'
  
  
  @property
  def todayOpenedAttendance(self):
    attendance = list(filter(lambda data: data.isToday == True ,self.attendance.all()))
    return attendance
  
  @property
  def openedCourse(self):
   
    _attendance = [ attendance for attendance in self.attendance.all() if attendance.isTimeOut == False ]
    
    return _attendance[0]
  
  @property
  def all_attendance(self):
    return list(map(lambda data: data, self.attendance.all()))
    
class Student(models.Model):
  id=models.AutoField(primary_key=True)
  level = models.IntegerField(blank=True)
  department = models.CharField(max_length=200, blank=True)
  courses = models.ManyToManyField(to=Course, related_name='courses')
  
  def __str__(self):
    return f'Student {self.id}'
  
  
  @property
  def coursesTaken(self):
    courses = [course.code for course in self.courses.all()]
    return courses
  
class Lecturer(models.Model):
  id=models.AutoField(primary_key=True)
  courses = models.ManyToManyField(to=Course, related_name='lecturer_courses')
  
  def __str__(self):
    return f'Lecture {self.id}'
  
  

  
  
  

  

  