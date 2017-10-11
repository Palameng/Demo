from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
