from .import views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
 
 
 path('',views.register, name ='register'), 
 path('home',views.index, name ='home'), 
 path('login',views.user_login, name ='login'), 
 path('about',views.about, name ='about'),
 path('contact',views.contact, name ='contact'),
 path('logout',views.logout_user, name ='logout'), 
  
 path('reset_pass',auth_views.PasswordResetView.as_view(template_name = "passwordreset.html"), name='reset_password'), 
 path('reset_pass_sent',auth_views.PasswordResetDoneView.as_view(template_name = "passwordresetsent.html"), name='password_reset_done'), 
 
 path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "passwordresetform.html"), name='password_reset_confirm'), 


 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]