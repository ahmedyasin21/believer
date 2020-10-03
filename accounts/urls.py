from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name ='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('verified/',views.VerifyEmailView.as_view(),name ='verify'),
    path('sent/<int:pk>',views.SentView.as_view(),name ='sent_confirm'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name ='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name = 'password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name ='password_reset_complate'),
    path('activate/<uidb64>/<token>/',views.ActivateAccount.as_view(), name='activate'),
    # path('profile/', views.ProfileView.as_view(),name = 'profile')
    # path('user',views.userprofile,name='home')
]



