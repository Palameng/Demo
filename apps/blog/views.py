import markdown
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views import View
from .models import Article, Tag, Category, Comment
from .forms import MyForm
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class MainIndexView(View):
    """
    博客主首页
    """
    def get(self, request):

        # 获取所有文章
        all_articles = Article.objects.all().order_by('-add_time')

        # 对所有A进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 第二个参数代表每一页显示的个数
        p = Paginator(all_articles, 3, request=request)
        articles = p.page(page)

        # 获取标签
        # tags = Tag.objects.all()

        # 获取分类
        # all_categorys = Category.objects.all()

        # 获取最新文章
        # flash_articles = Article.objects.all().order_by('-add_time')[:3]

        return render(request, 'blog/full-width.html', {
            "all_articles": articles,
            # "all_categorys": all_categorys,
            # "tags": tags,
            # "flash_articles": flash_articles,
        })


class IndexView(View):
    """
    博客个人首页
    """
    def get(self, request):

        # 获取所有文章
        all_articles = Article.objects.all()

        # 对所有A进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 第二个参数代表每一页显示的个数
        p = Paginator(all_articles, 3, request=request)
        articles = p.page(page)

        # 获取标签
        tags = Tag.objects.all()

        # 获取分类
        all_categorys = Category.objects.all()

        # 获取最新文章
        flash_articles = Article.objects.all().order_by('-add_time')[:3]

        return render(request, 'blog/index.html', {
            "all_articles": articles,
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

        # 获取评论
        all_article_comment = Comment.objects.filter(article_id=int(article_id))
        comment_nums = all_article_comment.count()
        post.comment_nums = comment_nums

        # 引入 markdown 模块
        post.content = markdown.markdown(post.content, extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])

        post.save()

        return render(request, 'blog/markdownToc.html', {
            "post": post,
            "tags": tags,
            "flash_articles": flash_articles,
            "all_categorys": all_categorys,
            "all_article_comment": all_article_comment,
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


class WriteArticlePageView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'blog/write_article.html', {
            "form": form,
        })


class WriteArticleView(View):
    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            article = Article()
            tag = Tag()
            article.content = form.cleaned_data.get("content")
            article.topic = form.data.get("name")
            tag.name = form.data.get("tag")
            tag.save()
            article.save()
            article.tags.add(tag)
            # print(text)
        else:
            pass
        return HttpResponseRedirect(reverse("index"))
