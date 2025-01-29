from django.db import models
import random
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

def get_random_price():
    return random.randint(10000, 999999)

class Article(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=get_random_price)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    