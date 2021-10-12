from django.shortcuts import HttpResponseRedirect, reverse


def belong_to_group(func):
  def middleware_wrapper(request, *args, **kwargs):
    # print(request.user.groups.filter(name='allowed_student'))
    if len(request.user.groups.filter(name='allowed_student')) <= 0:
      return HttpResponseRedirect(reverse('student:incomplete_student'))
    else:
      return func(request, *args, **kwargs)
  
  return middleware_wrapper