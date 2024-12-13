from rest_framework import serializers
from .models import Article, Comment, Clap

class ArticleSerializer(serializers.ModelSerializer):
    clap_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = '__all__'