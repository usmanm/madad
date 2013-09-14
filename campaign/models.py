from django.db import models

from utils.models import BaseModel

class Campaign(BaseModel):
  name = models.TextField(null=False, blank=False)
  start_date = models.DateField(null=False, blank=False)
  end_date = models.DateField(null=False, blank=False)
