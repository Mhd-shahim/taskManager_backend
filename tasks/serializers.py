from rest_framework import serializers
from .models import tasks

class TaskSerializer(serializers.ModelSerializer):  # Renamed to singular
    class Meta:
        model = tasks
        fields = '__all__'