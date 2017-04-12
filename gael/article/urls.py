# Create your url here.
# @author: Binoy
# @create_date: 10-Apr-2017
# @modified by: Binoy M V    
# @modified_date: 12-Apr-2017
# @linking to other page: /__init__.py
# @description: url of the article


from django.conf.urls import url
from . import views
from rest_framework import routers
from article.views import ArticleViewSet, ArticleImageViewSet, ArticleCategoryViewSet, article_list, article_detail, search_news
import os.path
from django.conf.urls import handler404, handler500

#defining the site media path
site_media = os.path.join(
    os.path.dirname(__file__), 'article_images'
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'images', ArticleImageViewSet)
router.register(r'category', ArticleCategoryViewSet)

urlpatterns = [
    
    url(r'^$', article_list, name='index'),
    url(r'^([0-9]+)/$', article_detail, name='Cloud Edit'),
    url(r'^search', search_news, name='search_news'),
]
 
urlpatterns += router.urls
handler404 = 'article.views.handler404'
