from django.contrib import admin

from social.models import User, DonationActivity, FollowActivity, CampaignCreateActivity

class UserAdmin(admin.ModelAdmin):
  pass

admin.site.register(User, UserAdmin)

class DonationActivityAdmin(admin.ModelAdmin):
  pass

admin.site.register(DonationActivity, DonationActivityAdmin)

class FollowActivityAdmin(admin.ModelAdmin):
  pass

admin.site.register(FollowActivity, FollowActivityAdmin)

class CampaignCreateActivityAdmin(admin.ModelAdmin):
  pass

admin.site.register(CampaignCreateActivity, CampaignCreateActivityAdmin)
