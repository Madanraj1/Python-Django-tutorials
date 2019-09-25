from django.urls import path
from . import views 
 
urlpatterns = [

    path('', views.Comment_page , name='comment_page'),

]