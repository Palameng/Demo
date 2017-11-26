"""Demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from Demos.settings import MEDIA_ROOT
from users.views import IndexView


urlpatterns = [

    url(r'^markdownx/', include('markdownx.urls')),

    url(r'^admin/', admin.site.urls),

    # index page
    url('^$', IndexView.as_view(), name="index"),

    # User
    url(r'^users/', include('users.urls', namespace="users")),

    # Blog
    url(r'^blogs/', include('blog.urls', namespace="blogs")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 测试Ueditor
    url(r'^ueditor/', include('DjangoUeditor.urls')),

]
