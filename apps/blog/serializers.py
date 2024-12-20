from rest_framework import serializers
from .models import Article, Comment, Clap, Follow

class ArticleSerializer(serializers.ModelSerializer):
    clap_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    view_count = serializers.SerializerMethodField()
    is_clapped = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    @staticmethod
    def get_clap_count(obj):
        claps = obj.article_claps.all()
        count = 0
        for clap in claps:
            count += clap.count
        return count

    @staticmethod
    def get_comment_count(obj):
        count = obj.article_comments.all().count()
        return count

    @staticmethod
    def get_view_count(obj):
        return obj.article_views.all().count()

    def get_is_clapped(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            clap = obj.article_claps.filter(author=request.user).first()
            if clap:
                return True
        return False

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'