from django.contrib import admin

from campaign.models import Campaign

class CampaignAdmin(admin.ModelAdmin):
  pass

admin.site.register(Campaign, CampaignAdmin)
