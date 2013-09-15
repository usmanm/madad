from django.db import models
from payments.models import Donation
from utils.models import BaseModel

class Campaign(BaseModel):
  name = models.TextField()
  tagline = models.TextField()
  description = models.TextField()
  image_url = models.URLField()
  needs = models.ManyToManyField(Donation, through='Need',
                                 related_name='needed_for')
  start_date = models.DateField()
  end_date = models.DateField()

class Need(BaseModel):
  need = models.ForeignKey(Donation)
  campaign = models.ForeignKey(Campaign)
  #substitution  factor
