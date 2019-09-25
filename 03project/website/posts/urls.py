from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView, name='homepage'),
    path('posts/',views.PostView, name='postview'),
]
