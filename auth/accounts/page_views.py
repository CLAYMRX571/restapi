from accounts.serializers import ArticleSerializer, ArticleDetailSerializer, CreateArticleSerializer
from .paginations import CustomPagination, MyPageNumberPagination, MyCursorPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from accounts.custom_filters import CustomArticleFilter
from rest_framework import serializers
from accounts.models import Article
from rest_framework import permissions

class ArticleListView(ListAPIView):
    """Bu view barchasini ko'rsatadi"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['author']
    # filterset_class = CustomArticleFilter
    search_fields = ['title', 'author__first_name']
    ordering_fields = ['price', 'created_at', 'id']

class ArticleDetailView(RetrieveAPIView):
    serializer_class = ArticleDetailSerializer 
    queryset = Article.objects.all()
    permission_classes = []
    # lookup_field = 'id'

class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    permission_classes = []

class ListCreateArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'author__first_name']
    ordering_fields = ['price', 'created_at', 'id']

class RetrieveUpdateDestroyArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = 'id'