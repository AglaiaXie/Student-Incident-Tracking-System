from django.conf.urls import include, url
from django.contrib import admin
import theme.views

urlpatterns = [
    url(r'^$', theme.views.home, name='home'),
    url(r'^ed4all/', include('ed4all.urls', namespace='ed4all')),
    url('r^admin/', admin.site.urls),

]
