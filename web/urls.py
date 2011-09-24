from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('web.views',
    (r'^$', 'news'),
    (r'^members$', 'members'),
    (r'^members/(?P<member_id>\d+)/$', 'memberDetail'),
    (r'^sponsors/$', 'sponsors'),
    (r'^contact/$', 'contact'),
    (r'^imprint/$', 'imprint'),
)
