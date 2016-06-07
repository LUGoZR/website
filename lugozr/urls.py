from django.conf.urls import url
from django.contrib import admin
from sajt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/([0-9]+)$', views.blog_post, name='blog_post'),
    url(r'^vest/([0-9]+)$', views.news_post, name='news_post'),
    url(r'^event/$', views.events),
    url(r'^event/([0-9]+)$', views.event_detail, name='event_detail'),
    # url(r'^event/([0-9]+)/prijava$', views.event_join, name='event_join') #TODO
]
