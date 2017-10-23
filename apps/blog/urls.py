from django.conf.urls import url, include
from blog.views import IndexView, DetailView

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='blog_index'),
    url(r'^detail/(?P<article_id>\d+)/$', DetailView.as_view(), name='article_detail'),
]
