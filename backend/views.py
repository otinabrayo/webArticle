from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsAuthor

def search_page(request):
    return render(request, 'search.html')

def register_page(request):
    return render(request, 'register.html')

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes =(TokenAuthentication, )
    permission_classes = [IsAuthenticated, IsAuthor]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['title', 'content',]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticlePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

'''
class Register(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        """
        Override perform_create to handle the object creation
        similar to custom behavior with an if statement.
        """
        if serializer.is_valid():  # This check happens internally in `CreateAPIView`, but you can add extra logic here if needed.
            serializer.save()  # Saves the new user instance to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Instead of handling it here, errors are handled automatically by CreateAPIView
            # But if you want custom error handling, you can raise exceptions or modify as needed
            self.handle_error(serializer.errors)
'''

# class Register(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
