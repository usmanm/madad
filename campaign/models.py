from django.db import models

from payments.models import Donation
from utils.models import BaseModel

class Campaign(BaseModel):
  name = models.TextField()
  tagline = models.TextField(null=True, blank=True)
  description = models.TextField()
  image = models.ImageField(upload_to='campaign/')
  needs = models.ManyToManyField(Donation, through='Need',
                                 related_name='needed_for')
  start_date = models.DateField()
  end_date = models.DateField()
  user = models.ForeignKey('social.User', related_name='campaigns')

class Need(BaseModel):
  name = models.TextField(null=True, blank=True)
  donation = models.ForeignKey(Donation)
  campaign = models.ForeignKey(Campaign)

  @property
  def remaining(self):
    remaining = self.donation.amount
    for donation in self.campaign.donations.filter(user__isnull=False):
      ignore = False
      for x in ['money', 'hours', 'goods']:
        if not hasattr(self.donation, x + 'donation'):
          continue
        if not hasattr(donation, x + 'donation'):
          ignore = True
      if ignore:
        continue
      remaining -= donation.amount
    return remaining
  
  @property
  def fulfilled(self):
    return self.donation.amount - self.remaining

  @property
  def fulfilled_percent(self):
    return (self.fulfilled * 100) / self.donation.amount
