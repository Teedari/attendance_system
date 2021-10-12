from django.db import models

# Create your models here.


class StaffNumber(models.Model):
  staff_id = models.CharField(max_length=10)
  taken = models.BooleanField(default=False)
  created_at  = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{}-{}'.format(self.staff_id, self.created_at)
  
  
class StudentNumber(models.Model):
  student_id = models.CharField(max_length=10)
  taken = models.BooleanField(default=False)
  created_at  = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{}-{}'.format(self.student_id, self.created_at)
  
  

  

