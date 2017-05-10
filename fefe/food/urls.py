from django.conf.urls import url

from .views import *

urlpatterns = [

    # url(r'^$', Index.as_view(), name='index'),
    url(r'^$', index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<param_area>\w+)/$', jeju_list , name='jeju'),
]
