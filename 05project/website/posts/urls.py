from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView, name='index'),
    path('contact/', views.ContactView, name='contact'),
]
