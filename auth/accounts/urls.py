from django.urls import path 
# from . import views
# from . import token_views as views
from . import jwt_token as views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
#    path('api/login/', views.LoginView.as_view(), name='login'),
   path('api/logout/', views.LogoutView.as_view(), name='logout'), 
   path('api/profile/', views.UserInfoView.as_view(), name='profile'),
]

urlpatterns += [
    path('api/token/custom', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]