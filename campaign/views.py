import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from campaign.models import Campaign, Need
import  datetime

def campaign(request, campaign_id):
  campaign = Campaign.objects.get(hash_id=campaign_id)
  needs = Need.objects.filter(campaign=campaign).all()
  needs_status = {}
  for need in Need.objects.filter(campaign=campaign).all():
    target = need.donation.amount
    needs_status[need] = (need.fulfilled, target , need.fulfilled*100/target)

  time_percentage_elapsed = ((datetime.date.today() - campaign.start_date).total_seconds() * 100)/(campaign.end_date - campaign.start_date).total_seconds()
  
  return render_to_response(
    'campaign/viewcampaign.html', 
    RequestContext(request, {'campaign':campaign,
                             'needs': needs,
                             'needs_status':needs_status,
                             'time_elapsed':time_percentage_elapsed}))

def needs(request, campaign_id):
  campaign = Campaign.objects.get(hash_id=campaign_id)
  needs = Need.objects.filter(campaign=campaign).all()
  return HttpResponse(
    json.dumps({need.hash_id: [float(need.fulfilled),
                               float(need.donation.amount)]
                for need in needs}))

@login_required
def create_campaign(request, user_id):
  return render_to_response('campaign/createcampaign.html')

def donate_money(request, user_id):
  return None
