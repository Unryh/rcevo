from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<slug>[-_\w]+)/$', views.news_details, name='news_details'),
    # url(r'^news/(?P<slug>[a-zA-Z0-9_-]{3,16})/$', views.news_details, name='news_details'),
    #login_user
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),

]
