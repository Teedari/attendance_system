from django.utils import timezone

def setTimeOut(minutes=10):
  result = timezone.timedelta(minutes=minutes) + timezone.now()
  time = str(result.time())[0:5]
  return time


