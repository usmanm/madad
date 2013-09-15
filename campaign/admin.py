from django.contrib import admin

from campaign.models import Campaign, Need

class CampaignAdmin(admin.ModelAdmin):
  pass

admin.site.register(Campaign, CampaignAdmin)

class NeedAdmin(admin.ModelAdmin):
  pass

admin.site.register(Need, NeedAdmin)
