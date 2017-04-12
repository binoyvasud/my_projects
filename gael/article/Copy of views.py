from __future__ import unicode_literals
from io import BytesIO
  
from django.contrib.auth.models import User
from django.test import TestCase
# from rest_framework.compat import patterns, url
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.test import  APIClient #APIRequestFactory
  

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Article, ArticleImage, ArticleCategory
from .serializers import ArticleSerializer, ArticleImageSerializer, ArticleCategorySerializer
from django.shortcuts import render, render_to_response
from django.template import RequestContext
# from requests.api import request
from rest_framework.test import APIClient
import json, datetime, random
from django.conf import settings
import random


#setting the base url
APIURL = settings.API_URL

# create api client object
client = APIClient()

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = []
        title = self.request.query_params.get('title', None)
        if title is not None:
            print "----------------"
            queryset = Article.objects.all()
            queryset = queryset.filter(title__icontains=title)
        else:
            queryset = Article.objects.all()
        return queryset

class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    print "hai2"
    serializer_class = ArticleImageSerializer

class ArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    
def ArticleList(request):
    response = client.get(APIURL  + '/articles/?format=json')
    parser = json.loads(response.content)
    preview_article = random_article(parser)
    print APIURL  + '/articles/?format=json'
    next_read = read_next()
     
    return render_to_response('article/article_list.html', {'articlelist':parser, 'preview_article': preview_article, 'next_read': next_read}, RequestContext(request))
    
def ArticleDetail(request, id):
    response = client.get(APIURL  + '/articles/' + id + '/?format=json')
    parser = json.loads(response.content)
    next_read = read_next()
     
    return render_to_response('article/details.html', {'article':parser, 'next_read': next_read}, RequestContext(request))
     
def random_article(article):
    print "#######################################################" 
    article_number = random.randint(0,len(article))
    article_number = int(article_number) - 1 
    print article_number
    print article[article_number]
    return article[article_number]
    print "#######################################################222"
    

def read_next():
    response = client.get(APIURL  + '/articles/?format=json')
    parser = json.loads(response.content)
    return parser
    


def search_news(data):
    print 'data', data
    response = client.get(APIURL  + '/articles/?format=json')
    parser = json.loads(response.content)
    return render_to_response('article/search_result.html', {'articlelist':parser}, RequestContext(request))
    


# # Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'article/article_list.html'
#     context_object_name = 'article_list'
#      
#     def get_queryset(self):
#         try:
#             return Article.objects.filter(title=self.request.GET['search'],)
#         except Exception, e:
#             return Article.objects.filter()
#          
# class DetailView(generic.DetailView):
#     model = Article
#     context_object_name = 'article_detail'
#     template_name = 'article/detail.html'
