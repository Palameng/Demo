from django.db import models

# Create your models here.


from DjangoUeditor.models import UEditorField


class Blog(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Content = UEditorField(
        verbose_name="内容",
        width=600,
        height=300,
        toolbars="full",
        imagePath="courses/ueditor/",
        filePath="courses/ueditor/",
        upload_settings={"imageMaxSize": 1204000},
        # settings={},
        # command=None,
        # event_handler=myEventHander(),
        # blank=True
        )

