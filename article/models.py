from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# class ArticleFirstType(models.Model):
#     name = models.CharField('名称', max_length=200)
#     created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "article_first_type"
#         verbose_name = "文章第一类别"
#         verbose_name_plural = verbose_name
#
#
# class ArticleSecondType(models.Model):
#     first_type = models.ForeignKey(ArticleFirstType, on_delete=models.CASCADE,
#                                    related_name="article_second_types",
#                                    verbose_name='第一类别')
#     name = models.CharField('名称', max_length=200)
#     created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "article_second_type"
#         verbose_name = "文章第二类别"
#         verbose_name_plural = verbose_name
from django.db.models import F, Max
from django.utils import timezone


class ArticleType(models.Model):
    name = models.CharField('名称', max_length=200)
    priority = models.IntegerField("优先级", default=-1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "article_type"
        ordering = ['priority']
        verbose_name = "文章类别"
        verbose_name_plural = verbose_name
    
    def save(self, *args, **kwargs):
        if self.priority == -1:
            
            if ArticleType.objects.count() == 0:
                self.priority = 1
            else:
                self.priority = ArticleType.objects.all().aggregate(Max('id')).get("id__max") + 1
        qt = ArticleType.objects.filter(priority=self.priority)
        if qt.count() > 0 and qt[0].id != self.id:
            ArticleType.objects.filter(priority__gte=self.priority).update(priority=F('priority') + 1)
        
        super().save(*args, **kwargs)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="论文题目")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="论文作者")
    img = models.ImageField(upload_to="image/%Y%m%d/", verbose_name="论文配图", blank=True, null=True)
    content = RichTextUploadingField(verbose_name="论文内容")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, related_name="articles",
                                     verbose_name='文章类别')
    status = models.BooleanField(default=True, verbose_name="是否存在")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "article"
        ordering = ['-updated']
        
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name
