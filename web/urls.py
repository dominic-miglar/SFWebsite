from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'web.views.news', name='news'),
    url(r'^members$', 'web.views.members', name='members'),
    url(r'^members/(?P<member_id>\d+)/$', 'web.views.memberDetail', name='memberdetails'),
    url(r'^sponsors/$', 'web.views.sponsors', name='sponsors'),
    url(r'^contact/$', 'web.views.contact', name='contact'),
    url(r'^imprint/$', 'web.views.imprint', name='imprint'),
)
