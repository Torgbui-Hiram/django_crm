from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.register_user, name='register'),
    path('auth', views.user_auth, name='sign_inn'),
    path('logout', views.signout_user, name='sign_out'),
    path('recovery', views.reset_password, name='pass_recovery'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # Django password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


]
