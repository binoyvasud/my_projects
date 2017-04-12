# Create your Model here.
# @author: Binoy
# @create_date: 10-Apr-2017
# @modified by: Binoy M V    
# @modified_date: 12-Apr-2017
# @linking to other page: /__init__.py
# @description: Models of the article

from __future__ import unicode_literals
from django.db import models

# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the model for the Article Category


class ArticleCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Category"
        db_table = "article_category"

    def __unicode__(self):
        return '%s ' % (self.name)
    
    
# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the model for the Article


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published On')
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    hero_image = models.ImageField(upload_to='article_images', default='None')
    description = models.TextField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "article"

    def __unicode__(self):
        return self.title

# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the model for the Article Image


class ArticleImage(models.Model):
    artile = models.ForeignKey(Article)
    image_name = models.CharField(max_length=200)
    article_image = models.ImageField(upload_to='article_images', default='None')

    class Meta:
        verbose_name = "Article Images"
        verbose_name_plural = "Article Images"
        db_table = "article_images"

    def __unicode__(self):
        return '%s ' % (self.image_name)
    
    
