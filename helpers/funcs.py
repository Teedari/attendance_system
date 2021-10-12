import datetime
import pytest
import uuid
from django.utils import timezone


def separate_fullname(name):
  first_name = ''
  last_name = ''
  isFirstSpace = False
  for char in name:
    if isFirstSpace:
      last_name+= char
      continue
    
    if char == ' ':
      isFirstSpace=True
      
    first_name+= char
    
  return {'first_name': first_name.strip(), 'last_name': last_name.strip()}
      
    
def test_separate_fullname():
  name = separate_fullname('Godfred Dari')
  assert 'Godfred' == name['first_name']
  assert 'Dari' == name['last_name']
  
  
# def generateStaffID(key='STAFF'):
#   uuid
  
  




def form_errors_decoder(errs, option=None):
  errs = errs.as_data()
  err_list = {}
  keys = tuple(errs.keys())
  for i in range(len(errs)):
    
    if option != None and option == keys[i]:
      continue
    
    err_list[keys[i]] = tuple(errs[keys[i]][0])[0]
  return {
    'keys': keys,
    'errors': err_list
  }
 



def form_error(val, errs):
  if val not in form_errors_decoder(errs)['keys']:
    return ;
  return form_errors_decoder(errs)['errors'][val]
  


def getUserType(username, key):
  return username.strip().lower().startswith(key)

def userTypeGenerator(username):
  if getUserType(username, 'staff'):
    return 'staff'

  if getUserType(username, 'ue'):
    return 'student'
  
  if not getUserType(username, 'staff') and not getUserType(username, 'ue'):
    return;
    
  

def test_get_user_type():
  assert getUserType('STAFF1232', 'staff') == True
  
  
def convertTimeFromStr(timeStr):
  hours = timeStr[0:2]
  mins = timeStr[-2:]
  return timezone.timedelta(hours=int(hours), minutes=int(mins))


def validateTimer(timeStr):
  time = str(timezone.datetime.now().time())[0:5]
  print(time)
  return convertTimeFromStr(time) > convertTimeFromStr(timeStr)


  
  