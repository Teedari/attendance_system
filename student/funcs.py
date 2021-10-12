from django.utils import timezone

def attendance_already_taken(students:list, name:str):
  if students == []: return False
  return True if name in students else False


def convertTimeFromStr(timeStr):
  hours = timeStr[0:2]
  mins = timeStr[-2:]
  return timezone.timedelta(hours=int(hours), minutes=int(mins))


def validateTimer(timeStr):
  time = timezone.datetime.now().strftime('%H:%m')
  return convertTimeFromStr(time) > convertTimeFromStr(timeStr)
