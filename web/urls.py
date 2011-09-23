urlpatterns = patterns('web.views',
    (r'^$', 'news'),
    (r'^(?P<member_id>\d+)/$', 'memberdetail'),

