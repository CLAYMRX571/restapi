from django.urls import path
from .views import ArticleView, UpdateArticleView, RetrieveArticleView, DestroyArticleView, ListArticleView, ArticleAPIView, ArticleListView, ClapApiView, CommentCreateView, CommentListApiView, ArticleListApiView, FollowApiView

urlpatterns = [
    # path('article_create/', ArticleView.as_view(), name='article'),
    # path('article_update/<int:pk>', UpdateArticleView.as_view(), name='update'),
    # path('article_retrieve/<int:pk>', RetrieveArticleView.as_view(), name='retrieve'),
    # path('article_list/', ListArticleView.as_view(), name='list'),
    # path('delete/<int:pk>', DestroyArticleView.as_view(), name='delete'),
    path('article/<int:pk>', ArticleAPIView.as_view(), name='article'),
    path('list/', ArticleListView.as_view(), name='list_create'),
    path('article_list/', ArticleListApiView.as_view(), name='article_list'),
    path('clap/', ClapApiView.as_view(), name='clap'),
    path('comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment_list/<int:pk>', CommentListApiView.as_view(), name='comment_list'),
    path('follow/<int:pk>', FollowApiView.as_view(), name='follow'),
]
