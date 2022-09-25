from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, 
                    UserPostListView, CategoryPostListView, CategoriesListView, CategoriesUpdateView,
                    CategoryCreateView, CategoryDeleteView)

#Passing through URL patterns to redirect to views
urlpatterns = [
    path('', PostListView.as_view(), name='app-index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),    
    path('about/', views.about, name='app-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/<str:category>', CategoryPostListView.as_view(), name='category-posts'),
    path('categories/', CategoriesListView.as_view(), name='category-list'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoriesUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    ]