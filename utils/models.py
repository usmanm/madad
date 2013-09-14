import uuid

from django.db import models

class Model(models.Model):
  class Meta:
    abstract = True # So that Django doesn't create a global `Model` table.

  hash_id = models.CharField(null=False, blank=False, max_length=36)
  date_created = models.DateTimeField(auto_now_add=True, null=False,
                                      blank=False)
  date_updated = models.DateTimeField(auto_now=True, null=False, blank=False)

  def save(self, *args, **kwargs):
    self.hash_id = str(uuid.uuid4()) # Random UUID.
    super(Model, self).save(*args, **kwargs)
