from twilio import twiml

from django_twilio.decorators import twilio_view

from campaign.models import Campaign
from payments.models import MoneyDonation
from social.models import User

@twilio_view
def sms_webhook(request):
  response = twiml.Response()
  phone =  request.POST.get('From')
  if not phone:
    return response
  user = User.objects.get(phone=phone)
  body = request.POST.get('Body')
  if not body:
    return response
  campaign_id, amount = map(lambda s: s.strip(), body.split(' '))
  campaign = Campaign.objects.get(hash_id=campaign_id)
  donation = MoneyDonation(campaign=campaign, user=user, amount=float(amount))
  donation.save()
  return response
