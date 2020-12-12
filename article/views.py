from rest_framework import filters, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from article.models import Article, ArticleFirstType, ArticleSecondType
from article.serializers import ArticleSerializer, ArticleFirstTypeSerializer, ArticleSecondTypeSerializer
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
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ("title", "content", "second_type__name")
    ordering_fields = ["id", "created", "updated", "second_type"]


class ArticleFirstTypeViewSet(BaseView):
    queryset = ArticleFirstType.objects.filter()
    serializer_class = ArticleFirstTypeSerializer


class ArticleSecondTypeViewSet(BaseView):
    queryset = ArticleSecondType.objects.filter()
    serializer_class = ArticleSecondTypeSerializer
