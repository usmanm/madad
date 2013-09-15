from django.db import models

from utils.models import BaseModel

class Campaign(BaseModel):
  name = models.TextField()
  tagline = models.TextField()
  description = models.TextField()
  image_url = models.URLField()
  start_date = models.DateField()
  end_date = models.DateField()
