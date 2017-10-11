from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .forms import LoginForm
from .models import UserProfile

from django.core.urlresolvers import reverse
import json
# Create your views here.


class LoginView(View):
    def get(self, request):

        return render(request, 'index.html', {

        })

    def post(self, request):
        login_form = LoginForm(request.POST)    # 此处传入一个字典

        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return render(request, "index.html")
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {'msg': '用户名未激活'})
            else:
                return render(request, "login.html", {'msg': '用户名或密码错误'})
        else:
            return render(request, "login.html", {"login_form": login_form})


class CustomBackend(ModelBackend):
    """
    当我们想要扩展校验条件时，可以重载authenticate方法，该方法需要：
        1）from django.contrib.auth.backends import ModelBackend

        2）在setting中加入：
        AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackend',  #加入支持的类

        )
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # user = UserProfile.objects.get(username=username)
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
