from django.conf.urls import url, include
from blog.views import IndexView, DetailView, ToTestMarkdownxView, WriteArticlePageView, WriteArticleView

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='blog_index'),
    url(r'^detail/(?P<article_id>\d+)/$', DetailView.as_view(), name='article_detail'),
    url(r'^test_markdown/$', ToTestMarkdownxView.as_view(), name='blog_test_markdown'),
    url(r'^get_articlepage/$', WriteArticlePageView.as_view(), name='get_articlepage'),
    url(r'^add_article/$', WriteArticleView.as_view(), name='add_article'),

]
