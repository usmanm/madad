import uuid

from django.db import models

class BaseModel(models.Model):
  class Meta:
    abstract = True # So that Django doesn't create a global `Model` table.

  hash_id = models.CharField(max_length=36, db_index=True)
  date_created = models.DateTimeField(auto_now_add=True, db_index=True)
  date_updated = models.DateTimeField(auto_now=True, db_index=True)

  def save(self, *args, **kwargs):
    self.hash_id = str(uuid.uuid4()) # Random UUID.
    super(BaseModel, self).save(*args, **kwargs)
