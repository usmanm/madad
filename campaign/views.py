from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from campaign.models import Campaign

def campaign(request, campaign_id):
  campaign = Campaign.objects.get(hash_id=campaign_id)
  needs_status = {}
  for need in campaign.needs:
    needs_status[need] = (need.fulfilled, need.target, need.fulfilled*100/need.target)
  return render_to_response('campaign/viewcampaign.html', {'campaign':campaign, 'needs_status':needs_status, 'money_status':money_status,})

@login_required
def create_campaign(request, user_id):
  return render_to_response('campaign/createcampaign.html')
