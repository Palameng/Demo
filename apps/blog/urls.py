from django.conf.urls import url, include
from blog.views import IndexView

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='blog_index'),
]
