from .serializers import PostSerializer
from .models import Post 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class ListCreatePostView(generics.ListCreateAPIView):
    model=Post
    
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    
@method_decorator(csrf_exempt, name='dispatch')
class RetrieveUpdateDestroyPostView(generics.RetrieveUpdateDestroyAPIView):
    model=Post
    serializer_class=PostSerializer
    queryset=Post.objects.all()   

