from django import forms
from markdownx.fields import MarkdownxFormField
from pagedown.widgets import AdminPagedownWidget
from markdownx.widgets import AdminMarkdownxWidget
from .models import Article


class MyForm(forms.Form):

    content = MarkdownxFormField()

    class Meta:
        model = Article
        fields = ['comment']


