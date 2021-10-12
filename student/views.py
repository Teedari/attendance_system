from django.http.response import HttpResponseRedirect
from django.utils import timezone
from student.forms import StudentCompletedForm
from student.decorators import belong_to_group
from django.shortcuts import render, reverse
from django.contrib.auth.models import Group
from auth_users.models import Profile
from attendance.models import Attendance, Course, MarkAttendance, Student
from django.http import JsonResponse
import datetime

from student.funcs import attendance_already_taken, validateTimer
# Create your views here.


def remove_user_group(_user):
  try:
    group = Group.objects.get(name = 'allowed_student')
    group.user_set.remove(_user)
  except:
      print('User does not belong to the group')
      return None
    
def add_user_group(_user):
  try:
    group = Group.objects.get(name = 'allowed_student')
    group.user_set.add(_user)
  except:
      print('User does not belong to the group')
      return None
    
  ##FIXME: create a final statement to create the above group and add student

def setTimeOut(minutes=10):
  print(datetime.datetime.now())
  return datetime.timedelta(minutes=minutes) + datetime.datetime.now()
  



@belong_to_group
def index(request):

  return render(request, 'student/index.html')



def incomplete_student(request):
  print(request.user)
  if request.method == 'POST':
    form = StudentCompletedForm(request.POST)
    
    if form.is_valid():
      student = Student.objects.create(level=form.cleaned_data.get('level'), department=form.cleaned_data.get('department'))
      student.save()
      profile = Profile.objects.get(user=request.user)
      profile.student = student
      profile.save()
   
      add_user_group(request.user)
      
      return HttpResponseRedirect(reverse('student:home'))
    
    print('Errors ', form.errors)
    
  return render(request, 'student/complete_student_form.html')


def registered_classes(request):
  context = {}
  profile = Profile.objects.get(user = request.user)
  context['courses'] = profile.student_courses
  return render(request, 'student/registered_classes.html', context)


def register_class(request):
  
  if request.method == 'POST' and request.is_ajax:
   code = request.POST['code']
   course = Course.objects.filter(code = code)[0]
   profile = Profile.objects.get(user=request.user)
  
   if(code in profile.student.coursesTaken):
      return JsonResponse({
      'status': 'fail',
      })
   
   profile.student.courses.add(course)
   profile.save()
   print(course, profile)
   return JsonResponse({
     'status': 'success',
   })

  return render(request, 'student/register_class.html')


def mark_attendance(request):
  print(request.user)
  context ={}
  
  if request.method == 'POST':
    id = request.POST.get('mark')
    _course = Course.objects.get(id=id)
    _attendance = MarkAttendance(user=request.user)
    _attendance.save()
    _course.attendances.add(_attendance)
    _course.save()
    
    return JsonResponse({'status': 'success'})
    
  profile = Profile.objects.get(user=request.user)
  courses = profile.student.courses.all()
  context['courses'] = courses
  return render(request, 'student/mark_attendance.html', context)


def find_course(request, id):
  course = None
  context = {}
  attendanceToday = None
  
  try:
    course = Course.objects.get(pk=id)
    context['course'] = course
 
  except:
    return HttpResponseRedirect(reverse('student:404'))
  # finally:
  
  try:
    attendanceToday = course.todayOpenedAttendance[0]
  except:
    context['err']  = 'You cannot mark attendance , session has expired'
    return render(request, 'student/find_course_for_attendance.html', context)

  if attendanceToday.isTimeOut:
    context['session_expired'] = True
    return render(request, 'student/find_course_for_attendance.html', context)
  else:
    
    if request.method == 'POST':
      
        if not attendanceToday.isTimeOut and not attendance_already_taken(attendanceToday.attendedStudents, request.user):
          
          att = MarkAttendance(user=request.user)
          att.save()
          attendanceToday.attendances.add(att)
          attendanceToday.save()
          
        else:
          
          if attendance_already_taken(attendanceToday.attendedStudents, request.user):
            context['err']  = 'Attendance already taken'
            
          else:
            context['err']  = 'Attendance access denied'
  
  return render(request, 'student/find_course_for_attendance.html', context)


def mark_attendance_record(request):
  context = {}
  course = Course.objects.filter(attendance__attendances__user=request.user)
  context['courses'] = course
  return render(request, 'student/mark_attendance_record.html', context)


def err404(request):
  return render(request, 'student/404.html')