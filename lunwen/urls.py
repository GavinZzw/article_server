"""lunwen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from article.views import ArticleViewSet, ArticleTypeViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('article', ArticleViewSet)
router.register('articleType', ArticleTypeViewSet)
# router.register('secondType', ArticleSecondTypeViewSet)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('ckeditor', include('ckeditor_uploader.urls')),
                  path('docs/', include_docs_urls(title="接口文档")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
