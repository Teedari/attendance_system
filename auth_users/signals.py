from attendance.models import Lecturer
from helpers.funcs import userTypeGenerator
from user_testing.models import StaffNumber, StudentNumber
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile



@receiver(post_save, sender=User)
def ProfileCreation(sender, created, instance, **kwargs):
  if created:
    print('User created', instance)
    profile = Profile.objects.create(user=instance)
    profile.fullname = '{} {}'.format(instance.first_name, instance.last_name)
    profile.user_role = 'staff' if instance.is_staff and instance.is_superuser else 'student'
    
    if instance.is_staff == True and instance.is_superuser == True:
      lecturer = Lecturer.objects.create()
      lecturer.save()
      profile.lecturer = lecturer
      print('Signals LECTURE ADDED ',lecturer)
    
    

    profile.save()
    