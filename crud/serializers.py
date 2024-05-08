from rest_framework import serializers

from crud.models import Todo


# This is 'TodoList objects serializer
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'content', 'created_at', 'is_completed']
