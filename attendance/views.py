from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from attendance.funcs import setTimeOut
from attendance.models import Attendance, Course
from auth_users.models import Profile
from helpers.funcs import form_errors_decoder
from .forms import CourseForm
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
  return render(request, 'attendance/index.html')


def course_added(request):
  print('USER: ', request.user)
  context = {}
  if request.method == 'POST':
    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
      try:
        profile = Profile.objects.get(user=request.user)
        f =  form.save()
        print(f)
        profile.lecturer.courses.add(f)
        profile.save()
      except :
          print('PROFILE DOES NOT EXITS')
     
    context['errs'] = form_errors_decoder(form.errors, 'username')
    context['hasError'] = True if context['errs'] is None else False
  return render(request, 'attendance/course_add.html', context)


def course_listed(request):
  context = {}
  profile = Profile.objects.get(user = request.user)
  context['profile'] = profile
  return render(request, 'attendance/course_list.html', context)


def course_registered_students(request, pk):
  course = None
  context = {}
  
  try:
    course = Course.objects.get(pk=pk)
    context['course'] = course
    student = Profile.objects.filter(student__courses__code = course.code)
    context['students'] = student
    print(student)
  except:
    return HttpResponseRedirect(reverse('attendance:404'))
  
  if request.method == 'POST':
    ID = request.POST['studentID']
    print(ID)
    profile = get_object_or_404(Profile, id=ID)
    profile.student.courses.remove(course)
    profile.save()
    
    # user = User.objects.get(id = ID)
    # user.delete()
    #FIXME: write the delete function 

  
  return render(request, 'attendance/course_registered_students.html', context)


def course_attendance(request, pk):
  course = None
  context = {}
  try:
    course = Course.objects.get(pk=pk)
    context['course'] = course
    # student = course.attendance[0].attendances.all()
    # context['students'] = student
    # print(student)
  except:
    return HttpResponseRedirect(reverse('attendance:404'))
  
  _allAttendance = course.all_attendance
  context['all_attendance'] = _allAttendance
    
  if request.method == 'POST':
    duration = int(request.POST['duration'])
    time = setTimeOut(minutes=duration)
    if len(course.todayOpenedAttendance) > 0 :
      todayAttendance = course.todayOpenedAttendance[0]
      todayAttendance.time_limit = time
      todayAttendance.accessible = True
      todayAttendance.save()
      print('ATTENDANCE UPDATED')
    else:
      attendance = Attendance(time_limit=time, accessible=True)
      attendance.save()
      
      course.attendance.add(attendance)
      course.save()
      
      print('ATTENDANCE CREATED')


  return render(request, 'attendance/course_attendance.html', context)




def err404(request):
  return render(request, 'attendance/404.html')
