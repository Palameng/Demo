# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from users.views import LoginView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='user_login'),
]
