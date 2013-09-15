from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Campaign, Need
def campaign(request, campaign_id):
  campaign = Campaign.objects.get(hash_id=campaign_id)
  needs = Need.objects.filter(campaign=campaign).all()
  needs_status = {}
  for need in Need.objects.filter(campaign=campaign).all():
    target = need.remaining + need.fulfilled
    needs_status[need] = (need.fulfilled, target , need.fulfilled*100/target)
  return render_to_response(
    'campaign/viewcampaign.html', 
    RequestContext(request, {'campaign':campaign,
                             'needs': needs,
                             'needs_status':needs_status}))

@login_required
def create_campaign(request, user_id):
  return render_to_response('campaign/createcampaign.html')

def donate_money(request, user_id):
  return None
