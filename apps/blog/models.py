from django.db import models
from apps.base.models import BaseModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.

class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles')
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(validators=[FileExtensionValidator(
        allowed_extensions=['img', 'jpg', 'jpeg', 'png', 'svg', 'webp'])], 
        upload_to="articles/", null=True, blank=True)
    
    def __str__(self):
        return self.title

class Comment(BaseModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_comment', null=True)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')

class Clap(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_claps')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_claps')
    count = models.IntegerField(default=1)