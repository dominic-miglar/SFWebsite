from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'streetfighters.web.views.news', name='news'),
    url(r'^members/$', 'streetfighters.web.views.members', name='members'),
    url(r'^members/(?P<member_id>\d+)/$', 'streetfighters.web.views.memberDetail', name='memberdetails'),
    url(r'^sponsors/$', 'streetfighters.web.views.sponsors', name='sponsors'),
    url(r'^contact/$', 'streetfighters.web.views.contact', name='contact'),
    url(r'^imprint/$', 'streetfighters.web.views.imprint', name='imprint'),
)
