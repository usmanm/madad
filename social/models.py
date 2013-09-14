from django.contrib.auth.models import AbstractUser
from django.db import models

from campaign.models import Campaign
from payments.models import Donation
from utils.models import BaseModel

class User(AbstractUser):
  location = models.CharField(max_length=256, null=True, blank=True)
  follows = models.ManyToManyField('User', related_name='followers')
  supports = models.ManyToManyField(Campaign, related_name='supporters')

class Activity(BaseModel):
  user = models.ForeignKey(User, related_name='activities')
  liked_by = models.ManyToManyField(User, related_name='likers')

class DonationActivity(Activity):
  donation = models.ForeignKey(Donation)
  campaign = models.ForeignKey(Campaign)

class FollowActivity(Activity):
  followed_user = models.ForeignKey(User)
