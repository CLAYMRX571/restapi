from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['id', 'title']
    list_per_page = 20

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'user']
    list_per_page = 20
