from django.urls import path
from .views import index, course_added, course_listed, course_attendance,course_registered_students, err404

app_name = 'attendance'

urlpatterns = [
  path('', index, name='home'),
  path('course/add',course_added, name='course_add' ),
  path('course/list',course_listed, name='course_list' ),
  path('course/student/registered/<int:pk>',course_registered_students, name='course_registered_students' ),
  path('course/attendance/<int:pk>',course_attendance, name='course_attendance' ),
  path('page/not/found', err404, name='404')
]