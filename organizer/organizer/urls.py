"""organizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import HomeView
from allauth.account.views import logout
from allauth.socialaccount.providers.discord.views import oauth2_login, oauth2_callback

urlpatterns = [
    path('home', HomeView.as_view()),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),

    # path('accounts/', include('allauth.urls')), ## don't include all allauth urls
    path('accounts/logout/', logout, name="account_logout"),
    path('accounts/discord/login/', oauth2_login, name="discord_login"),
    path('accounts/discord/login/callback/', oauth2_callback, name="discord_callback"),


]
