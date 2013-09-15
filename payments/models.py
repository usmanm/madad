from django.db import models

from utils.models import BaseModel

class Donation(BaseModel):
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  user = models.ForeignKey('social.User', related_name='donations',
                           null=True, blank=True)
  campaign = models.ForeignKey('campaign.Campaign', related_name='donations')

  def save(self):
    super(Donation, self).save()
    if not self.user:
      return
    from social.models import DonationActivity
    donation_activity = DonationActivity(user=self.user,
                                         donation=self)
    donation_activity.save()

class MoneyDonation(Donation):
  pass

class GoodsDonation(Donation):
  name = models.CharField(max_length=256)

class HoursDonation(Donation):
  schedule = models.TextField() # Serialized JSON.
