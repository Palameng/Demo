# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from users.views import LoginView, LogoutView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='user_login'),
    url('^logout/$', LogoutView.as_view(), name="logout"),
]
