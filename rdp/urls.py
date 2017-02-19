from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^download/(?P<software_name>[\w]+)/?$', views.download_view, name='download')
]

