from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

