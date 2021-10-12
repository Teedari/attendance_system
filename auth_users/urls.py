from django.urls import path
from .views import index, registerLecturer, registerStudent, logoutUser


app_name = 'auth_users'


urlpatterns = [
  path('', index, name='sign_in'),
  path('register/staff', registerLecturer, name='sign_up_staff'),
  path('register/student', registerStudent, name='sign_up_student'),
  path('logout', logoutUser, name='sign_out'),
]