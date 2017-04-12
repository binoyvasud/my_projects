# @author: Binoy
# @create_date: 10-Apr-2017
# @modified by: Binoy M V    
# @modified_date: 12-Apr-2017
# @linking to other page: /__init__.py
# @description: Methods for the context processor

#Importing the configurations
from django.conf import settings 

def baseUrl(request):
    """To clean the site url
    Args:
        {
            self - request from the page
        }
            
    Returns:
        Returns response to the html page
            
    Raises:
        Exceptions                
    """
    return {'base_url': settings.BASE_URL}

def mediaRoot(request):
    """To find the media root
    Args:
        {
            self - request from the page
        }
            
    Returns:
        Returns response to the html page
            
    Raises:
        Exceptions                
    """
    return {'media_root': settings.MEDIA_ROOT}
