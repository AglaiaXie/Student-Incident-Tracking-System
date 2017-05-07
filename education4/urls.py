from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^$', theme.views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^ed4all/', include('ed4all.urls', namespace='ed4all')),
    #url(r'^ed4all/', include('django.contrib.auth.urls')),
    # url(r'^users/', include('users.urls', namespace='users')),

]
