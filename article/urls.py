from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^1/', views.basic_one),
    url(r'^2/', views.template_two),
    url(r'^3/', views.template_three),
    url(r'^articles/all/$', views.articles),
    url(r'^articles/post/(?P<article_id>[0-9]+)/$', views.article),
    url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', views.addlike),
    url(r'^articles/addcomment/(?P<article_id>[0-9]+)/$', views.addcomment),
    url(r'^page/(\d+)/$', views.articles),
    url(r'^', views.articles),

]