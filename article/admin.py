from django.contrib import admin

from article.models import Article, ArticleType


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "updated", "article_type", "status")
    search_fields = ("title", "content")


@admin.register(ArticleType)
class ArticleFirstTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "priority")
    search_fields = ("name",)

# @admin.register(ArticleFirstType)
# class ArticleFirstTypeAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)
#
#
# @admin.register(ArticleSecondType)
# class ArticleSecondTypeAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)
