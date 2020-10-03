"""islamic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(template_name = 'base.html'),name = 'home'),
    path('index/',views.IndexView.as_view(template_name = 'index.html'),name = 'index'),#extra cloning template
    path('about/',views.AboutView.as_view(template_name = 'about.html'),name = 'about'),
    path('accounts/', include('accounts.urls',namespace = 'accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('dashboard/',views.TestPage.as_view(),name = 'test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),

    path('thankyou/',views.Thanksbeingpart.as_view(),name='thankyou'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

    path('videos/', include('videos.urls',namespace = 'videos')),
    path('notes/', include('notes.urls',namespace = 'notes')),

    # path('yes/',views.SomeListView.as_view(),name ='yes'),

    path('quiz/', include('quiz.urls',namespace='quiz')),

    # path('youtube/', include('django_youtube.urls')),
    #navbar stuff
    path('videos/',views.VideosView.as_view(template_name ='pages/videos.html'),name = 'videos')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
