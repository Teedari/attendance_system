from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.



class Test(TestCase):
  
  
  def setUp(self):
    u = User.objects.create(username='STAFF12345', password='12345678').save()
    
    
  def test_user_created(self):
    u = User.objects.get(username='STAFF12345')
    p = Profile.objects.get(user__username='STAFF12345')
    self.assertEqual(u.username , 'STAFF12345')
    self.assertTrue(p is not None, True)
    self.assertTrue(p.lecturer is not None, True)
    
  def test_course_created(self):
    p = Profile.objects.get(user__username='STAFF12345')
    
