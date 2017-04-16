from django.conf.urls import patterns, url
from django.contrib import admin
from ed4all import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^course_view/(?P<pk>\d+)$', views.course_view, name='course_view'),
    url(r'^course_new$', views.course_create, name='course_new'),
    url(r'^course_edit/(?P<pk>\d+)$', views.course_update, name='course_edit'),
    url(r'^course_delete/(?P<pk>\d+)$', views.course_delete, name='course_delete'),

    url(r'^review_new/(?P<parent_pk>\d+)$', views.review_create, name='review_new'),
    url(r'^review_edit/(?P<pk>\d+)$', views.review_update, name='review_edit'),
    url(r'^review_delete/(?P<pk>\d+)$', views.review_delete, name='review_delete'),

]