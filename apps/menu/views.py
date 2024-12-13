from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
# Create your views here.

class TaskAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskRetrieveAPIView(APIView):   
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskUpdateSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer