"""
URL configuration for BookStoreProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_initial_page, name="initial"),
    path('home', views.show_home_page, name="index"),
    path('about', views.show_about_page, name="about"),
    path('contacts', views.show_contacts_page, name="contacts"),
    path('log-in', views.show_log_in, name="log in"),
    path('register', views.show_register, name="register")
]
