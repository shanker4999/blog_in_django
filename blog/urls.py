from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register',views.register,name='register'),
    url(r'^login',views.user_login,name='user_login'),
    url(r'^logout',views.user_logout,name='user_logout'),
    url(r'article/(?P<year>[0-9]{4})/$', views.year_archive, name='year_archive'),
    url(r'^comment/(?P<article_id>[0-9]+)/$', views.comment, name='comment'),
    url(r'article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month_archive'),
    url(r'(?P<article_id>[0-9]+)/$',views.article_detail,name='article_detail'),

    url(r'^contact',views.contact,name='contact'),
]