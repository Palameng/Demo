from django import forms
from markdownx.fields import MarkdownxFormField
from pagedown.widgets import AdminPagedownWidget
from markdownx.widgets import AdminMarkdownxWidget
from .models import MyModel


class MyForm(forms.Form):

    test = MarkdownxFormField()

    class Meta:
        model = MyModel
        fields = ['test']


