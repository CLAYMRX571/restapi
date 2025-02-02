from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Article, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
     
    class Meta:
        model = Article
        fields = ['id', 'title', 'price', 'author']

class ArticleCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.first_name or obj.user.username
    
    def get_time(self, obj):
        return obj.created_at.strftime('%H:%M %d.%m.%Y')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'time']

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    comments = ArticleCommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'price', 'content', 'created_at', 'updated_at', 'author', 'comments']

class CreateArticleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%H:%M %d.%m.%Y", read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Article
        fields = ['id','title', 'price', 'content', 'author', 'created_at']
    
    def validate_content(self, value):
        if len(value) < 25:
            raise serializers.ValidationError('Content must be at 25')
        return value

    def validate_title(self, value):
        if len(value) < 15:
            raise serializers.ValidationError('Title must be at 15')
        return value 
    
    def validate(self, data):
        if data['price'] < 10000:
            raise serializers.ValidationError('Price must be at 10000')
        return data

    def create(self, validated_data):
        article = Article.objects.create(**validated_data)
        return article

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password('123')
        user.save()
        return user
    
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email', read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email 
        return data