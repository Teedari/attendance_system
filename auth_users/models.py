from attendance.models import Lecturer, Student
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
  id = models.AutoField(primary_key=True)
  fullname = models.CharField(max_length=100)
  user = models.ForeignKey( on_delete=models.CASCADE, to=User)
  student = models.ForeignKey(to=Student, related_name='student', on_delete=models.CASCADE, blank=True, null=True)
  lecturer = models.ForeignKey(to=Lecturer, related_name='lecturer', on_delete=models.CASCADE, blank=True, null=True)
  user_role = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.user} - {self.fullname}'
  
  
  @property
  def level(self):
    return self.student.level
  
  @property
  def department(self):
    return self.student.department
  
  @property
  def lecturer_courses(self):
    return self.lecturer.courses.all()
  
  @property
  def student_courses(self):
    return self.student.courses.all()