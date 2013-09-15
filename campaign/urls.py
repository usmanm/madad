from django.conf.urls import patterns, url

urlpatterns = patterns('campaign.views',
    url(r'viewcampaign/(?P<campaign_id>[a-zA-Z0-9_\+-]+)$', 'campaign'),
    url(r'createcampaign$', 'create_campaign'),
    url(r'donatemoney', 'donate_money'),
)

