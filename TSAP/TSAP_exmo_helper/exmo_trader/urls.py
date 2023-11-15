"""exmo_trader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from et_app import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about), 
    path("about/currents/", views.currents), 
    path("about/current_pairs/", views.current_pairs), 
    path("about/prices_only/", views.current_prices), 
    path("cur_forms/", views.cur_forms),
    path("cur_forms_answer/", views.cur_forms_answer),
    path("cur_pair_forms/", views.cur_pair_forms),
    path("cur_pair_forms_answer/", views.cur_pair_forms_answer),
]
