from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return JsonResponse({'error': 'Blog does not exist'}, status=404)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        blog.delete()
        return JsonResponse({'success': True})

