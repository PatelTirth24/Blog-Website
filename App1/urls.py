from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('about-us/',about_us,name='about-us'),
    path('Blog-Post-Details/<int:pk>',blog_post_details,name='Blog-Post-Details'),
    path('Latest-Blog-Post-Details/<int:pk>',lat_blog_post_details,name='Latest-Blog-Post-Details'),
    path('Blog-Post/',blog_post,name='Blog-Post'),
    path('special-offer/',special_offer,name='special-offer'),
    path('team/',team,name='team'),
    path('contact/',B_contact,name='contact'),

]
