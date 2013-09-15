from django.conf.urls import patterns, include, url

from django.contrib import admin; admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/$', 'website.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social.urls')),
    url(r'^campaign/', include('campaign.urls')),
    url(r'^$', 'website.views.index'),
)
