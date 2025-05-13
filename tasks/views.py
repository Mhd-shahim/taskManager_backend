from rest_framework.views import APIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import tasks



# Create your views here.
class createTask(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class taskView(APIView):
    def get(self, request, id=None):
        if id:
            task = get_object_or_404(tasks, pk=id)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            all_tasks = tasks.objects.all()
            serializer = TaskSerializer(all_tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class TaskDelete(APIView):
    def post(self, request, id=None):
        if id:
            task = get_object_or_404(tasks, pk=id)
            task.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)