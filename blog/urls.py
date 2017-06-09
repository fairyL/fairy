from django.conf.urls import url
from blog import ajax, views

urlpatterns = [
    url(r'^(?P<burl>[\w\W\-]+)/$', views.detail, name='product_blog'),
]