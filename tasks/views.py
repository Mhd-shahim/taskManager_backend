from rest_framework.views import APIView
from .serializers import TaskSerializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import tasks



# Create your views here.
class createTask(APIView):
    def post(self, request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

