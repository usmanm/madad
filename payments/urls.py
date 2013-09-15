from django.conf.urls import patterns, url

urlpatterns = patterns('payments.views',
    url(r'twilio/sms/', 'sms_webhook'),
)
