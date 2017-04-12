# Create your views here.
# @author: Binoy
# @create_date: 10-Apr-2017
# @modified by: Binoy M V    
# @modified_date: 12-Apr-2017
# @linking to other page: /__init__.py
# @description: Functions of the article


from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Article, ArticleImage, ArticleCategory
from .serializers import ArticleSerializer, ArticleImageSerializer, ArticleCategorySerializer
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import json, datetime, random
from django.conf import settings
import random
import requests
from django.http import Http404
import logging

#setting the base url
APIURL = settings.API_URL
COUNT  = settings.COUNT_MIN_LIMIT 
COUNT_MAX  = settings.COUNT_MAX_LIMIT 

# Get an instance of a logger
logger = logging.getLogger(__name__)

# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the API for the Article
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Article.objects.all().order_by('-id')
        title = self.request.query_params.get('title', None)
        limit = self.request.query_params.get('limit', None)
        random = self.request.query_params.get('random', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title).order_by('-id')
        elif limit is not None:
            queryset = queryset[:limit]
        elif random is not None:
            queryset = queryset[COUNT:COUNT_MAX]
        return queryset

# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the API for the Article Image
class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ArticleImage.objects.all()
        id = self.request.query_params.get('artile_id', None)
        if id is not None:
            queryset = queryset.filter(artile_id=id)
        return queryset

# @author: Binoy
# @create_date: 12-Apr-2017
# @modified by: Binoy M V
# @modified_date: 12-Apr-2017
# @description: Creating the API for the Article category
class ArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


def article_list(request):
    """To get the article list
        Args:
            {
                request - request from the page
            }
            
        Returns:
            Returns response to the html page
            
        Raises:
            Exceptions
    """
    try:
        logger.info('Calling the api' + APIURL  + '/articles/?format=json&limit=' + str(COUNT))
        response = requests.get(APIURL  + '/articles/?format=json&limit=' + str(COUNT))
        parser = json.loads(response.content)
        preview_article = random_article(parser)
        next_read = read_next()
        return render(request, 'article/article_list.html', {'articlelist':parser, 'preview_article': preview_article, 'next_read': next_read})
    except:
        logger.error('Calling the api error in article_list')
        raise Http404("Article does not exist")
    
    
def article_detail(request, id):
    """To get the article details
        Args:
            {
                request - request from the page
                id - Id of the article
            }
            
        Returns:
            Returns response to the html page
            
        Raises:
            Exceptions 
    """
    try:
        logger.info('Calling the api' + APIURL  + '/articles/' + id + '/?format=json')
        response = requests.get(APIURL  + '/articles/' + id + '/?format=json')
        parser = json.loads(response.content)
        images = article_images(id)
        next_read = read_next()
        return render_to_response('article/details.html', {'article':parser, 'next_read': next_read, 'related_images': images}, RequestContext(request))
    except:
        logger.error('Calling the api error in article_detail')
        raise Http404("Article does not exist")
    
    
def article_images(id):
    """To get the article images of a particular article
        Args:
            {
                id - Id of the article
            }
            
        Returns:
            Returns response to the html page
            
        Raises:
            Exceptions
    """
    try:
        query_string = '&artile_id='+str(id)
        logger.info('Calling the api' + APIURL  + '/images/?format=json'+query_string)
        response = requests.get(APIURL  + '/images/?format=json'+query_string)
        parser = json.loads(response.content)
        return parser
    except:
        logger.error('Calling the api error in article_images')
        raise Http404("Article image does not exist")
     
def random_article(article):
    """To show the random article as preview
        Args:
            {
                id - article list
            }
            
        Returns:
            Returns response to the html page
            
        Raises:
            Exceptions
    """
    try:
        article_number = random.randint(0,len(article))
        article_number = int(article_number) - 1 
        return article[article_number]
    except:
        raise Http404("Article image does not exist")

def read_next():
    """To show the article in the what to read next section
        Args:
            {   
            }
            
        Returns:
            Returns article details as json
            
        Raises:
            Exceptions
    """
    try:
        response = requests.get(APIURL  + '/articles/?format=json&random=yes')
        parser = json.loads(response.content)
        return parser
    except:
        raise Http404("Article does not exist")


def search_news(request):
    """To show the article with the search functionality
        Args:
            {   
            }
            
        Returns:
            Returns response to the html page
            
        Raises:
            Exceptions
    """
    try:
        query_string = ''
        if request.GET['search_text'].strip() != '':
            query_string = '&title='+request.GET['search_text']
        response = requests.get(APIURL  + '/articles/?format=json'+query_string)
        parser = json.loads(response.content)
        return render_to_response('article/search_result.html', {'articlelist':parser})
    except:
        raise Http404("Search Item error")


def handler404(request):
    """
    Function to show custom page to handle 404
    Args:
        {
            request - request from the page
        }
    Returns:
            Returns - html template
    Raises:
        NA
    """
    
    #Setting the variable and template page for the 500 error
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    """
    Function to show custom page to handle 500
    Args:
        {
            request - request from the page
        }
    Returns:
        Returns - html template
    Raises:
        NA
    """
    
    #Setting the variable and template page for the 500 error
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response