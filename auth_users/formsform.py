from user_testing.models import StaffNumber, StudentNumber
from helpers.funcs import separate_fullname, userTypeGenerator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class CustomUserForm(forms.ModelForm):
  class Meta: 
    model = User
    fields = ['first_name', 'username', 'email', 'password']
    
    
  # def clean(self):
  #   cleaned_data = super().clean()
  #   user_role = userTypeGenerator(cleaned_data.get('username'))
  #   print(user_role)
  #   UserIDs =  StaffNumber.objects.filter(staff_id=cleaned_data.get('username')) if user_role == 'staff' else StudentNumber.objects.filter(student_id=cleaned_data.get('username'))
    
  #   # UserIDs = StaffNumber.objects.filter(staff_id=cleaned_data.get('username'))
    
  #   IDType = ''
    
  #   if user_role == 'staff':
  #     IDType = 'Staff'
  #   elif user_role == 'student':
  #     IDType = 'Student'
  #   else:
  #     IDType = 'Unknown'
    
  #   if UserIDs is None:
  #     raise ValidationError('{} ID is incorrect'.format(IDType))
    
  #   if UserIDs[0].taken:
  #     raise ValidationError('{} ID already exist'.format(IDType),code='ID exists')
    
  #   try:
  #     if User.objects.filter(email = cleaned_data.get('email')).exists():
  #       raise ValidationError('Email already exist', code='email exists')
  #   except:
  #     raise ValidationError('Email already exist', code='email exists')
    
  def save(self, commit=True):
    _instance = super().save(commit=False)
    name = separate_fullname(_instance.first_name)
    _instance.first_name = name.get('first_name')
    _instance.last_name = name.get('last_name')
    _instance.set_password(self.cleaned_data.get('password'))
    _instance.is_staff = True
    print('FORMS save')
    if commit:
      _instance.save()
      
      
class CustomLoginForm(forms.Form):
  username = forms.CharField(max_length=10)
  password = forms.CharField(max_length=200)
  
  
  
  def validate(self):
    data = super().validate()
    if len(data > 10):
      raise ValidationError('Username exceeds 10 charaters')
    
    return data
    
    
  def save(self, commit=True):
    cleaned_data = super().save(commit=False)
    
    print('LOGIN FORM')
    
    if commit:
      print('Commited')
    
    
  
    