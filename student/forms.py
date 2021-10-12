from django import forms




class StudentCompletedForm(forms.Form):
  level = forms.CharField(max_length=3)
  department = forms.CharField(max_length=100)
  