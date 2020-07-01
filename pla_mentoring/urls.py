"""pla_mentoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from .views import (
    home_page_view,
)

from account.views import (
    registration_view,
    profile_view,
    login_view,
    logout_view,
)

from network.views import (
    add_alumni_response_view,
    alumni_response_view,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name="home"),
    path('accounts/login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('chat/', include('chat.urls')),
    path('alumni/', include('network.urls')),
    path('students/', include('students.urls')),
    path('profile/<user_id>/', profile_view, name="profile"),
    path('response/add/', add_alumni_response_view, name="add_response"),
    path('response/<alum_id>/', alumni_response_view, name="view_response"),
    path('register/', registration_view, name="register"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
