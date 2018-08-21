from django.conf.urls import url, include  
from . import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^donation/$',views.donation, name='donation'),
    url(r'^donation/pensioner/$',views.donation_pensioner, name='donation_pensioner'),
    url(r'^donation/poor/$',views.donation_poor, name='donation_poor'),
    url(r'^donation/child/$',views.donation_child, name='donation_child'),
    url(r'^donation/churches/$',views.donation_churches, name='donation_churches'),
    url(r'^donation/prisoners/$',views.donation_prisoners, name='donation_prisoners'),
    url(r'^donation/mercy/$',views.donation_mercy, name='donation_mercy'),
    url(r'^project/create/$',views.create_page, name='create'),
    url(r'^project/(?P<pk>\d+)/$', views.project, name='project'),
    url(r'^project_verifi/$', views.verifi_list, name='verifi_list'),
    url(r'^project/(?P<pk>\d+)/publish/$', views.publish_project, name='publish_project'),
    url(r'^project/(?P<pk>\d+)/delete/$', views.delete_project, name='delete_project'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^blog/create/$', views.creates_blog, name='create_blog'),
    url(r'^blog/(?P<pk>\d+)/$',views.created_blog,name='created_blog'),
    url(r'^blog/$', views.blog_list, name='blog_list'),
    url(r'^comment/(?P<pk>\d+)/approve2/$', views.comment_approve2, name='comment_approve2'),
    url(r'^comment/(?P<pk>\d+)/remove2/$', views.comment_remove2, name='comment_remove2'),
]   
