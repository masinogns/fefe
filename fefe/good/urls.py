from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', goodIndex, name='index'),
    url(r'^list/(?P<pk>[0-9]+)/$', goodList, name = 'list'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', GoodDV.as_view(), name='detail'),
    url(r'^detail/(?P<pk>[0-9]+)/$', goodDetail, name='detail'),
    # url(r'^(?P<bssh_nma>\w+)/hhh$', blogPost, name='hhh'),
    # url(r'^hhh$', blogPost, name='hhh'),

]
