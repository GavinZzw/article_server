# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 12:19
# @Author  : zzw
# @File    : serializers.py
from rest_framework import serializers

from article.models import Article, ArticleFirstType, ArticleSecondType


class ArticleSerializer(serializers.ModelSerializer):
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'content', "updated", "second_type")


class ArticleSecondTypeSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = ArticleSecondType
        fields = "__all__"


class ArticleFirstTypeSerializer(serializers.ModelSerializer):
    # article_second_types = ArticleSecondTypeSerializer(many=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = ArticleFirstType
        fields = "__all__"
