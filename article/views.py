from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from article.models import Article, ArticleType
from article.serializers import ArticleSerializer, ArticleTypeSerializer
from utils.response import ApiResponse


class MyPageNumberPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 10
    # 获取URL参数中设置的每页显示数据条数
    page_size_query_param = 'size'
    
    # 获取URL参数中传入的页码key
    page_query_param = 'page'
    
    # 最大支持的每页显示的数据条数
    max_page_size = 100


class BaseView(mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs).data
        return ApiResponse(data=data)
    
    def retrieve(self, request, *args, **kwargs):
        data = super().retrieve(request, *args, **kwargs).data
        return ApiResponse(data=data)


class ArticleViewSet(BaseView):
    queryset = Article.objects.filter(status=True)
    serializer_class = ArticleSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ("article_type",)
    search_fields = ("title", "content", "article_type__name")
    ordering_fields = ["id", "created", "updated", "article_type"]


class ArticleTypeViewSet(BaseView):
    queryset = ArticleType.objects.filter()
    serializer_class = ArticleTypeSerializer
