from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Article, Clap, Comment
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ArticleSerializer, ClapSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
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
        if (item.author == request.user):
            data = request.data 
            serializer = self.serializer_class(instance=item, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data)
        else:
            data = {
                'status': False,
                'message': "Ushbu maqolaning muallifi siz emas!"
            }
            raise ValidationError(data)

    def delete(self, request, pk):
        item = self.model.objects.get(id=pk)
        if (item.author == request.user):
            item.delete()
            return Response({"msg":"successfully deleted!"})
        else:
            data = {
                'status': False,
                'message': "Ushbu maqolaning muallifi siz emas!"
            }
            raise ValidationError(data)

class ArticleListView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny, )
    model = Article

    def post(self, request):
        if request.user.is_authenticated:
            data = request.data
            data['author'] = request.user.id 
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data)
        else:
            data = {
                'status': False,
                'message': "Siz ro'yxatdan o'tmagansiz!"
            }
            raise ValidationError(data)

    def get(self, request):
        serializer = self.serializer_class(instance=self.model.objects.all(), many=True)
        return Response(data=serializer.data)

class ClapApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user_id = request.user.id
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

    def post(self, request):
        data = request.data
        data['author'] = request.user.id 
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class CommentListApiView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        comments = Comment.objects.filter(article=self.kwargs['pk'])
        return comments