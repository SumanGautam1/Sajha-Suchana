from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('feedback/',feedback,name='feedback'),
    path('news/',news,name='news'),
    path('about/',about,name='about'),
    path('government/',government,name='government'),
    path('notices/',notices,name='notices'),
    path("search/",searchGov, name="searchGov"),

    # Khalti URLS
    
    path('initiate',initkhalti,name="initiate"),
    # path('verify',verifyKhalti,name="verify")
]
