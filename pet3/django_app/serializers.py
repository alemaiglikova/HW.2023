from rest_framework import serializers
from .models import User, News


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'author', 'created_at']