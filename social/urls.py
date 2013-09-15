from django.conf.urls import patterns, url

urlpatterns = patterns('social.views',
    url(r'user/(?P<user_id>[a-zA-Z0-9_\+-]+)$', 'user'),
    url(r'login/$', 'login'),
    url(r'signup/$', 'login'),
)
