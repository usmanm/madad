from django.conf.urls import patterns, url

urlpatterns = patterns('campaign.views',
    url(r'(?P<campaign_id>[a-zA-Z0-9_\+-]+)$', 'campaign'),
)

