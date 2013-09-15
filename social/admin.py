from django.contrib import admin

from social.models import User, Activity

class UserAdmin(admin.ModelAdmin):
  pass

admin.site.register(User, UserAdmin)

class ActivityAdmin(admin.ModelAdmin):
  pass

admin.site.register(Activity, ActivityAdmin)
