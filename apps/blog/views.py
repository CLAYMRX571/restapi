from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Article, Clap, Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ArticleSerializer, ClapSerializer, CommentSerializer
from rest_framework.permissions import AllowAny 
# Create your views here.

class ArticleView(CreateAPIView):
    queryset = Article.objects.filter(is_active=True)
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )

class UpdateArticleView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )

class RetrieveArticleView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )

class DestroyArticleView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )

class ListArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )

class ArticleAPIView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )
    model = Article

    def get(self, request, pk):
        item = self.model.objects.get(id=pk)
        serilizer = self.serializer_class(instance=item)
        data = {
            'data': serilizer.data
        } 
        return Response(data=data)

    def put(self, request, pk):
        item = self.model.objects.get(id=pk)
        data = request.data 
        serializer = self.serializer_class(instance=item, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        item = self.model.objects.get(id=pk)
        item.delete()
        return Response({"msg":"successfully deleted!"})

class ArticleListView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )
    model = Article

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def get(self, request):
        serializer = self.serializer_class(instance=self.model.objects.all(), many=True)
        return Response(data=serializer.data)

class ClapApiView(APIView):
    def post(self, request):
        user_id = request.data.get('author')
        article_id = request.data.get('article')
        claps = Clap.objects.filter(author = user_id, article=article_id)
        if claps.exists():
            clap = claps.first()
            clap.count += 1
            clap.save()
            serializer = ClapSerializer(instance=clap)
        else:
            serializer = ClapSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(data=serializer.data) 

class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()

class CommentListApiView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        comments = Comment.objects.filter(article=self.kwargs['pk'])
        return comments

    
