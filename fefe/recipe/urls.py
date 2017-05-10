from django.conf.urls import url

from .views import *

urlpatterns = [

    # url(r'^$', RecipeIndex.as_view(), name='index'),
    url(r'^$', index, name='index'),
    url(r'^(?P<ty_code>\w+)/$', recipeList, name = 'list'),
    url(r'^detail/(?P<recipe_id>[0-9]+)/$', recipeDetail, name='detail'),
    # url(r'^survey$', GoodSurvey.as_view(), name='survey'),

]
