from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from social.models import Activity, User

@login_required
def user(request, user_id):
  user = User.objects.get(username=user_id)
  if request.user.is_authenticated():
    follows = user.followers.filter(username=request.user.username).exists()
  else:
    follows = False
  return render_to_response(
    'social/profile.html', 
    RequestContext(
      request, 
      {'profile_user': user,
       'activities': user.activities.order_by('-date_created'),
       'follows': follows
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
