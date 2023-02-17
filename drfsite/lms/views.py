from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializer import CourseSerializer

class CourseAPIView(APIView):
    def get(self, request):
        w = Course.objects.all()
        return Response({'posts ': CourseSerializer(w, many=True).data})

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Course.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CourseSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Delete method not allowed'})
        try:
            instance = Course.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects dont exist'})
        instance.delete()
        return Response({'post': 'delete post ' + str(pk)})



# class CourseAPIView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer