from django.db import models

from utils.models import BaseModel

class Campaign(BaseModel):
  name = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
