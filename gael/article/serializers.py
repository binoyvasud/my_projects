# Create your rest framework serializer here.
# @author: Binoy
# @create_date: 10-Apr-2017
# @modified by: Binoy M V    
# @modified_date: 12-Apr-2017
# @linking to other page: /__init__.py
# @description: rest framework serializer of the article

from rest_framework import serializers
from .models import Article, ArticleCategory, ArticleImage

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'category_id', 'hero_image', 'description')

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('id', 'image_name', 'article_image', 'artile_id')

        
class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ('id', 'name', 'description')
