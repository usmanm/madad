from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from social.models import Activity

@login_required
def user(request, user_id):
  return render_to_response(
    'social/profile.html', 
    RequestContext(
      request, 
      {'user': request.user,
       'activities': request.user.activities.order_by('-date_created')
       }))

def login(request):
  if request.user.is_authenticated():
    return redirect(user, user_id=request.user.username)
  return render_to_response('social/login.html')

def signup(request):
  return render_to_response('social/signup.html')

@login_required
def like_activity(request, activity_id):
  activity = Activity.objects.get(hash_id=activity_id)
  activity.liked_by.add(request.user)
