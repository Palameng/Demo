# -*- coding: utf-8 -*-
from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    """
    html中name的名称必须和这里的一致，否则无法校验
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


