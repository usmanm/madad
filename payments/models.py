from django.db import models
from website import User

# Create your models here.
class Payment(models.Model):
	payment_type = models.CharField(max_length=200)
	