from django.conf.urls import url
from core import ajax, views

urlpatterns = [
    url(r'^$', views.index, name='core_index'),
    url(r'^postsignin/$', ajax.signin, name='core_postsignin'),
    url(r'^postlogin/$', ajax.login, name='core_postlogin'),
    url(r'^login/$', views.login, name='core_login'),
]