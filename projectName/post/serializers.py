from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    title = serializers.CharField(max_length=255)
    niche = serializers.CharField(max_length=60)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    body = serializers.CharField()
    
    
    def create(self, validated_data):
        return Post.objects.create(** validated_data)
   
    def update(self, instance, validated_data):
        instance.title= validated_data.get('title',instance.title)
        instance.niche = validated_data.get('niche',instance.niche)
        instance.author = validated_data.get('author', instance.author)
        instance.body= validated_data.get('body',instance.body)
        instance.save()
        return  instance
