from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from .serializers import PostSerializer
from .models import Post 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status

# create a function
def home(request):
     
    return HttpResponse("<h1>Welcome to GeeksforGeeks</h1>")

@csrf_exempt
def postApi(request):
    if (request.method == 'GET'):
        jData = request.body
        stream = io.BytesIO(jData)
        
        print(stream.getvalue())
        
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
    
    
    if (request.method == 'POST'):
        jdata = request.body
        stream = io.BytesIO(jdata)
        pydata = JSONParser().parse(stream)
        serializer = PostSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is created'}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata, content_type='application/json')
        # If not valid
        jdata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jdata, content_type='application/json')
    
    if request.method == 'PATCH':
        jdata = request.body
        stream = io.BytesIO(jdata)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Post.objects.get(id=id)
        serializer = PostSerializer(stu, data=pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data are updated'}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata, content_type='application/json')
        jdata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jdata, content_type='application/json')   
    
    if request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        
                
        if(id is None):
            res = {'msg':'id is required'}
            
        try:
            stu = Post.objects.get(id = id)
        except Post.DoesNotExist:
            stu = None
                    
        if(stu is None):
            res = {'msg':'id not found'}
            jdata = JSONRenderer().render(res)
            return HttpResponse(jdata,content_type='application/json',
                                 status= status.HTTP_404_NOT_FOUND
                                
                                )
            
            
        else:
            stu.delete()
            res = {'msg':'Data was deleted !'}
        
        jdata = JSONRenderer().render(res)
        return HttpResponse(jdata,content_type='application/json',
                            
                           
                            )
    
@csrf_exempt
def getAllPosts(request):
    if(request.method == 'GET'):   
        
        stu = Post.objects.get()
        serializer = PostSerializer(stu, data=pydata, partial=True)
        
        

