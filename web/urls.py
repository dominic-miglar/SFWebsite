from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('web.views',
    url(r'^$', 'news', name='news'),
    url(r'^members$', 'members', name='members'),
    url(r'^members/(?P<member_id>\d+)/$', 'memberDetail', name='memberdetails'),
    url(r'^sponsors/$', 'sponsors', name='sponsors'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^imprint/$', 'imprint', name='imprint'),
)
