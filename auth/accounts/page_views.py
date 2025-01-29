from rest_framework.generics import ListAPIView
from rest_framework import serializers
from accounts.models import Article
from .paginations import CustomPagination, MyPageNumberPagination, MyCursorPagination
from django_filters.rest_framework import DjangoFilterBackend
from accounts.custom_filters import CustomArticleFilter
from rest_framework.filters import SearchFilter, OrderingFilter

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['author']
    filterset_class = CustomArticleFilter
    search_fields = ['title', 'author__first_name']
    ordering_fields = ['price', 'created_at', 'id']