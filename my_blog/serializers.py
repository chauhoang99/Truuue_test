from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "author")


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User()
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()

        return validated_data

