from django.urls import path
from rest_framework import routers
from .views import (
    TaskAPIView,
    TaskRetrieveAPIView,
    TaskListAPIView,
    TaskRetrieveUpdateAPIView,
    TaskViewSet,
)

router = routers.DefaultRouter()
router.register('line', TaskViewSet, basename="line")

urlpatterns = [
    path('task', TaskAPIView.as_view()),
    path('task/<int:pk>', TaskRetrieveAPIView.as_view()),
    path('tasks', TaskListAPIView.as_view()),
    path('tasked/<int:pk>', TaskRetrieveUpdateAPIView.as_view()),
]

urlpatterns += router.urls 
