from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.urls import path

app_name = 'quiz'
urlpatterns = [

    #   path('',views.WeekListView.as_view(),'week')

    path('week/', views.home, name = 'home'),
    path('result', views.result, name = 'result'),
    path('<str:choice>', views.questions, name = 'questions'),
]