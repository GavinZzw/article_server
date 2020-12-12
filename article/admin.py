from django.contrib import admin

from article.models import Article, ArticleFirstType, ArticleSecondType


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "updated", "second_type", "status")
    search_fields = ("title", "content")


@admin.register(ArticleFirstType)
class ArticleFirstTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ArticleSecondType)
class ArticleSecondTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
