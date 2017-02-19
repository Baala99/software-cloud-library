from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^rdp/', include('rdp.urls')),
    url(r'admin/', include.site.urls),
]
