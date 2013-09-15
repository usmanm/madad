from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

def campaign(request, campaign_id):
  #campaign = Campaign.objects.get(hash_id=campaign_id)
  needs = ['Legal','Accounting','Programming']
  needs_status = {'Legal': ('10', '30', 1000/30), 'Accounting': ('20', '50', 2000/50), 'Programming' : ('0', '100', 0/100),} #same order as needs
  money_status = ['1000', '4500']
  return render_to_response(
    'campaign/viewcampaign.html', 
    RequestContext(request,
                   {'needs':needs, 
                    'needs_status':needs_status, 
                    'money_status': money_status, 
                    'title': 'Hold', 'tagline': 'hold',
                    'description': 'description',
                    'image_url':'https://s3.amazonaws.com/ksr/assets/000/902/806/2ac9c3466559301081c2fdff4c154712_large.jpg?1378725565'
                    }))

@login_required
def create_campaign(request, user_id):
  return render_to_response('campaign/createcampaign.html')
