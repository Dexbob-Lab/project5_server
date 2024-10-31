from django.shortcuts import render
from django.http import HttpResponse 
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from question.serializers import QuestionSerializer, QuestionHitSerializer
from question.models import QuestionModel


def home(request):
    return HttpResponse("문의사항 게시판 서버 연결")


@api_view(['GET', 'POST'])
def question(request):
    if request.method == 'GET':
        data = QuestionModel.objects.all().order_by('-id')
        serializer = QuestionSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, id):
    try:
        data = QuestionModel.objects.get(id=id)
    except QuestionModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_search(request):
    query = request.query_params.get('search')
    condition = Q(id__icontains=query) | Q(title__icontains=query) | Q(contents__icontains=query) | Q(nickname__icontains=query)
    data = QuestionModel.objects.filter(condition).order_by('-id')
    serializer = QuestionSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_password(request):
    queryId = request.query_params.get('id')
    queryPw = request.query_params.get('pw')
    data = QuestionModel.objects.filter(id=queryId, password=queryPw)
    return Response(len(data), status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def question_hits(request, id):
    try:
        data = QuestionModel.objects.get(id=id)
    except QuestionModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = QuestionHitSerializer(data, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)