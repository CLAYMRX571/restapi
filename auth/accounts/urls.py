from accounts.page_views import ArticleListView, ArticleDetailView, ArticleCreateView, ListCreateArticleView, RetrieveUpdateDestroyArticleView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
# from . import token_views as views
from . import jwt_token as views
from .views import RegisterView
from django.urls import path 
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Rest Api",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="claymrx571@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('api/register/', RegisterView.as_view(), name='register'),
#  path('api/login/', views.LoginView.as_view(), name='login'),
   path('api/logout/', views.LogoutView.as_view(), name='logout'), 
   path('api/profile/', views.UserInfoView.as_view(), name='profile'),
]

urlpatterns += [
    path('api/token/custom', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('data/articles', ArticleListView.as_view()),
    path('data/articles/<int:pk>', ArticleDetailView.as_view()),
    path('data/create/', ArticleCreateView.as_view()),
    path('new/articles/', ListCreateArticleView.as_view()),
    path('new/articles/<int:pk>', RetrieveUpdateDestroyArticleView.as_view()),
]