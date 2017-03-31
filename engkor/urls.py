from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^definitions/$', views.get_definitions, name='get_definitions'),
    url(r'^definitions/(?P<id>[0-9]+)/$', views.get_definition, name='get_definition'),
    url(r'^definitions/(?P<word>.+)/$', views.get_definition_word, name='get_definition_word'),
]