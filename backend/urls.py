from django.urls import path
from .views import ArticleList, ArticlePost, search_page, register_page
urlpatterns = [
    path('articles/', ArticleList.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticlePost.as_view(), name='article-detail',),
    path('search/', search_page, name='search-page'),
    path('register/', register_page, name='register'),

]
