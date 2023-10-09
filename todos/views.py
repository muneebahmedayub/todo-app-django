from django.shortcuts import render
from rest_framework.views import APIView
from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TodoList(APIView, LimitOffsetPagination):
    """
    List all todos, or create a todo
    """

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        todos = Todo.objects.all()
        result = self.paginate_queryset(todos, request, view=self)
        serializer = TodoSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
