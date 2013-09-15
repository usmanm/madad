from django.shortcuts import render

from campaign.models import Campaign

def index(request):
  campaign = Campaign.objects.all()[0]
  return render(
    request,
    'website/index.html', 
    {'campaign': campaign})
