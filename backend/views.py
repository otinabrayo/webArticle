from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

# from rest_framework.permissions import IsAdminUser


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

