from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:id>/', views.PostDetailView, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:id>', views.CommentView, name='comment'),
]
