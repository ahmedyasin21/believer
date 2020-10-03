from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('list/',views.VideosListView.as_view(),name ='videos_playlist'),
    path('list/<str:list_title>/',views.VideosModelListView.as_view(),name ='list_videos'),
]