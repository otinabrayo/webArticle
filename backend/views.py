from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

def search_page(request):
    return render(request, 'search.html')

def register_page(request):
    return render(request, 'register.html')

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser, IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['title', 'content',]
    search_fields = ['title', 'content']

class ArticlePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
