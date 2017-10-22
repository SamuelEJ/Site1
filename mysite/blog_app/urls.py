from django.conf.urls import url
from django.db import models
from . import views
#from blog_app.views import PostMonthArchiveView

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.BlogPostDetail, name='BlogPostDetail'),
    url(r'^home', views.blogHome, name='blogHome'),


    #Pass parameter to blogSearchList view
    url(r'^search/(?P<text_name>\w+)/$', views.blogSearchList, name='blogSearchList'),
    #Pass GET query string to blogSearchList view
    url(r'^search/$', views.blogSearchList, name='blogSearchListQueryString'),
    #url(r'^search/$', views.blogSearchList, name='blogSearchList'),

    # Pass DATE parameter to blogSearchList view
    url(r'^search/(?P<yearParameter>\w+)/(?P<monthParameter>\w+)/$', views.blogSearchList, name='blogSearchListDates'),
    # Pass GET query string to blogSearchList view

    url(r'^$', views.index, name='index'),

    url(r'^view/(?P<id>[0-9]+)/$', views.BlogPostViewDetail, name='BlogPostViewDetail'),

    url(r'^archive/$', views.ArchiveView, name='ArchiveView'),





]
