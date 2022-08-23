from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrIsSuperUserOrReadOnly
# Create your views here.

class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.publishes.all()
    serializer_class = ArticleSerializer
    pagination_class=PageNumberPagination
    
class ArticleView(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Article.publishes.all()
    lookup_field='slug'
    serializer_class = ArticleSerializer
    pagination_class=PageNumberPagination
    permission_classes = [IsAuthorOrIsSuperUserOrReadOnly]




        


    
    

