from django.http.response import HttpResponseRedirect
from helpers.funcs import form_errors_decoder
from auth_users.forms import CustomAdminUserForm, CustomLoginForm, CustomStudentUserForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, reverse

# Create your views here.


def index(request):
  context = {}
  if request.method == 'POST':
    form = CustomLoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
      print(user)
      if user is not None:
        
        if user.is_superuser == True:
          user = login(request,user)
          return HttpResponseRedirect(reverse('attendance:home'))
        else:
          user = login(request,user)
          return HttpResponseRedirect(reverse('student:home'))
      # user = authenticate()
    context['errs'] = form.errors
  return render(request, 'auth/index.html', context)




def registerLecturer(request):
  context = {}
  if request.method == 'POST':
      form = CustomAdminUserForm(request.POST)
      if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse('auth_users:sign_in'))
      context['errs'] = form_errors_decoder(form.errors, 'username')
  return render(request, 'auth/register.html', context)



def registerStudent(request):
  context = {}
  if request.method == 'POST':
    form = CustomStudentUserForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('auth_users:sign_in'))
      
    context['errs'] = form_errors_decoder(form.errors, 'username')
  return render(request, 'auth/register_student.html', context)


def logoutUser(request):
  logout(request)
  return HttpResponseRedirect(reverse('auth_users:sign_in'))