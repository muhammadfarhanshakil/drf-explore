from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from .serializers import PostSerializer
from .models import Post 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

# create a function
def home(request):
     
    return HttpResponse("<h1>Welcome to GeeksforGeeks</h1>")


def postApi(request):
    if (request.method == 'GET'):
        jData = request.body
        stream = io.BytesIO(jData)
        pyData = JSONParser().parse(stream)
        
        id = pyData.get('id', None)
        
        if(id is not None):
            post = Post.objects.get(id=id)
            serializer=PostSerializer(post)
            jdata = JSONRenderer().render(serializer.data)
            return HttpResponse(jdata,content_type = 'application/json')
        
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)
        jdata = JSONRenderer().render(serializer.data)
        
        return HttpResponse(jdata,content_type = 'application/json')
        

