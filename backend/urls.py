from django.urls import path
from .views import ArticleList, ArticlePost

urlpatterns = [
path('articles/', ArticleList.as_view(), name='articles'),
path('articles/<int:pk>/', ArticlePost.as_view(), name='article-detail',)
]
