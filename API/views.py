from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializer

from .models import Task, User


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/user-list/',
        'Detail View': '/user-detail/<str:pk>/',
        'Create': '/user-create/',
        'Update': '/user-update/<str:pk>/',
        'Delete': '/user-delete/<str:pk>/',

        'TList': '/task-list/',
        'TDetail View': '/task-detail/<str:pk>/',
        'TCreate': '/task-create/',
        'TUpdate': '/task-update/<str:pk>/',
        'TDelete': '/task-delete/<str:pk>/',


    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')





# USER


@api_view(['GET'])
def userList(request):
    users = User.objects.all().order_by('-fb_id')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    print(request.__str__())
    try:
        print(User.objects.__str__())
        users = User.objects.get(fb_id=pk)
        print(type(users))
    except User.DoesNotExist:
        return Response(None)
    serializer = UserSerializer(users, many=False)
    print(serializer.data.__str__())
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    data = request.data

    try:
        users = User.objects.get(fb_id=data['fb_id'])
        return Response(None)
    except User.DoesNotExist:
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
    try:
        users = User.objects.get(fb_id=pk)
    except User.DoesNotExist:
        return Response(None)
    serializer = UserSerializer(instance=users, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
    try:
        user = User.objects.get(fb_id=pk)
    except User.DoesNotExist:
        return Response(None)
    user.delete()

    return Response('Item successfully delete')