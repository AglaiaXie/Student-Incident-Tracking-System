from django.conf.urls import url, include
from django.contrib import admin

import theme.views
import ed4all.urls

urlpatterns = {
    url(r'^$', theme.views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ed4all/', include('ed4all.urls', namespace='ed4all')),
}
