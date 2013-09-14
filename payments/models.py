from django.db import models

from utils.models import BaseModel

class Payment(BaseModel):
	payment_type = models.CharField(max_length=200)
	
