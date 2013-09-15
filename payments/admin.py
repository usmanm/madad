from django.contrib import admin

from payments.models import MoneyDonation, GoodsDonation, HoursDonation

class MoneyDonationAdmin(admin.ModelAdmin):
  pass

admin.site.register(MoneyDonation, MoneyDonationAdmin)

class GoodsDonationAdmin(admin.ModelAdmin):
  pass

admin.site.register(GoodsDonation, GoodsDonationAdmin)

class HoursDonationAdmin(admin.ModelAdmin):
  pass

admin.site.register(HoursDonation, HoursDonationAdmin)
