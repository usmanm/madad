from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from campaign.models import Campaign

def campaign(request, campaign_id):
  #campaign = Campaign.objects.get(hash_id=campaign_id)
  return render_to_response('campaign/viewcampaign.html', {'title':'Hold', 'tagline':'hold', 'description':'description'})

@login_required
def create_campaign(request, user_id):
  return render_to_response('campaign/createcampaign.html')
