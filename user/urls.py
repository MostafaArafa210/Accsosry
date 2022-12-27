
from django.urls import path,include
from user import  views
from django.contrib.auth import views as log
urlpatterns = [
#                    User Auth
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_info', views.profile_info, name='profile_info'),

    path('password_rest/', log.PasswordResetView.as_view(template_name='auth/rest_password.html'),name='password_reset'),
    path('password_reset_done/',log.PasswordResetDoneView.as_view(template_name='auth/password_reset_sent.html'),name='password_reset_done'),
    path('rest/<uidb64>/<token>', log.PasswordResetConfirmView.as_view(template_name='auth/password_reset_form.html'),name='password_reset_confirm'),
    path('password_reset_complete/', log.PasswordResetCompleteView.as_view(template_name='auth/password_reset_done.html'),name='password_reset_complete'),

]
