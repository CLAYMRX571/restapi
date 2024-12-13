from django.contrib import admin
from .models import Article, Clap, Comment
# Register your models here.

admin.site.register(Article)
admin.site.register(Clap)
admin.site.register(Comment)