from django.urls import path
from posts import views
urlpatterns = [
    path('',views.HomePageView, name='index'),
    path('posts/',views.PostView, name='posts_body')
]
