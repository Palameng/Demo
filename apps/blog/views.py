import markdown
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views import View
from .models import Article, Tag, Category, MyModel
from .forms import MyForm


class IndexView(View):
    """
    博客首页
    """
    def get(self, request):

        # 获取所有文章
        all_articles = Article.objects.all()

        # 获取标签
        tags = Tag.objects.all()

        # 获取分类
        all_categorys = Category.objects.all()

        # 获取最新文章
        flash_articles = Article.objects.all().order_by('add_time')[:3]

        return render(request, 'blog/index.html', {
            "all_articles": all_articles,
            "all_categorys": all_categorys,
            "tags": tags,
            "flash_articles": flash_articles,
        })


class DetailView(View):
    """
    博文详情页
    """
    def get(self, request, article_id):

        # 获取文章实例
        post = get_object_or_404(Article, pk=article_id)

        # 获取标签
        tags = Tag.objects.all()

        # 获取最新文章
        flash_articles = Article.objects.all().order_by('add_time')[:3]

        # 获取分类
        all_categorys = Category.objects.all()

        # 引入 markdown 模块
        post.content = markdown.markdown(post.content, extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return render(request, 'blog/single.html', {
            "post": post,
            "tags": tags,
            "flash_articles": flash_articles,
            "all_categorys": all_categorys,
        })


class ToTestMarkdownxView(View):
    def get(self, request):
        # markdown_test = MyModel.objects.get(id=1)
        # context = MyModel()
        form = MyForm()
        # context.test = form.cleaned_data.get("test")
        # context.save()

        return render(request, 'blog/test_markdownx.html', {
            # "markdown_test": markdown_test,
            "form": form,
        })

