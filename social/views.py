from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response

from social.models import Activity

def user(request, user_id):
  return render_to_response('base/base.html')

@login_required
def like_activity(request, activity_id):
  activity = Activity.objects.get(hash_id=activity_id)
  activity.liked_by.add(request.user)
