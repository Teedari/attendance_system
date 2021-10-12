from user_testing.models import StaffNumber, StudentNumber
from helpers.funcs import separate_fullname, userTypeGenerator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class CustomAdminUserForm(forms.ModelForm):
  class Meta: 
    model = User
    fields = ['first_name', 'username', 'email', 'password']
    
  def save(self, commit=True):
    _instance = super().save(commit=False)
    name = separate_fullname(_instance.first_name)
    _instance.first_name = name.get('first_name')
    _instance.last_name = name.get('last_name')
    _instance.set_password(self.cleaned_data.get('password'))
    _instance.is_staff = True
    _instance.is_superuser = True
    print('FORMS save')
    if commit:
      _instance.save()
      

class CustomStudentUserForm(forms.ModelForm):
  class Meta: 
    model = User
    fields = ['first_name', 'username', 'email', 'password']
    
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
  username = forms.CharField(max_length=200)
  password = forms.CharField(max_length=200)
    
    
  def save(self, commit=True):
    cleaned_data = super().save(commit=False)
    
    print('LOGIN FORM')
    
    if commit:
      print('Commited')
    
    
  
    