from django.urls import path
from .views import (BlogListView, 
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    )

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='edit'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='delete'),
]