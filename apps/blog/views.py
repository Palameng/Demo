import markdown
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views import View
from .models import Article


class IndexView(View):
    def get(self, request):
        all_articles = Article.objects.all()
        return render(request, 'blog/index.html', {
            "all_articles": all_articles,
        })


class DetailView(View):
    def get(self, request, article_id):
        post = get_object_or_404(Article, pk=article_id)
        # 记得在顶部引入 markdown 模块
        post.content = markdown.markdown(post.content, extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return render(request, 'blog/single.html', context={'post': post})
