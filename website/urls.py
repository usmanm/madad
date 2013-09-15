from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin; admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/$', 'website.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social.urls')),
    url(r'^campaign/', include('campaign.urls')),
    url(r'^$', 'website.views.index'),
)

if settings.DEBUG:
  from django.views.static import serve
  _media_url = settings.MEDIA_URL
  if _media_url.startswith('/'):
    _media_url = _media_url[1:]
    urlpatterns += patterns('',
                            (r'^%s(?P<path>.*)$' % _media_url,
                             serve,
                             {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
