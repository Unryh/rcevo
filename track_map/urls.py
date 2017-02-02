from django.conf.urls import url
from . import views

app_name = 'track_map'

urlpatterns = [
    url(r'^$', views.track_index, name='track_index'),
]