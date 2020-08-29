# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

app_name = "pages"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout', user_logout, name="logout"),
    path('dash/', dash_page, name="login"),


]
