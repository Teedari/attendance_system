from attendance.models import Course
from django import forms



class CourseForm(forms.ModelForm):
  
  class Meta:
    model = Course
    fields = '__all__'
    

      