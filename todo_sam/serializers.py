from rest_framework import serializers
from todo_sam.models import TodoModel

class Todoserializer(serializers.ModelSerializer):

    class Meta:

        model = TodoModel

        fields = "__all__"