from django.shortcuts import render
from django.http import HttpResponse 
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from notice.serializers import NoticeSerializer
from notice.models import NoticeModel

def home(request):
    return HttpResponse("공지사항 게시판 서버 연결")

@api_view(['GET', 'POST'])
def notice(request):
    if request.method == 'GET':
        data = NoticeModel.objects.all()
        serializer = NoticeSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def notice_detail(request, id):
    try:
        data = NoticeModel.objects.get(id=id)
    except NoticeModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NoticeSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NoticeSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def notice_search(request):
    query = NoticeModel.query_params.get('search')
    data = NoticeModel.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
    serializer = NoticeSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)