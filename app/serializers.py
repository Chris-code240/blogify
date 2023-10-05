from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from .models import BlogPost, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username','email','password','first_name','last_name']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BlogPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Comment
        fields = '__all__'
