from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^Counselor/add/$', views.CounselorCreate.as_view(), name='add-counselor'),
    url(r'^Counselor/view/$', views.CounselorRead.as_view(), name='view-counselor'),
    url(r'^Counselor/delete/(?P<pk>\w+)$', views.CounselorDelete.as_view(), name='delete-counselor'),
    url(r'^Counselor/update/(?P<pk>\w+)$', views.CounselorUpdate.as_view(), name='update-counselor'),
]
