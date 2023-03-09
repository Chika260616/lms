from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import CourseSerializer


class CourseAPIList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)


class CourseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)


class CourseAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)



#
#
# class CourseAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseAPIView(APIView):
#     def get(self, request):
#         w = Course.objects.all()
#         return Response({'posts ': CourseSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Course.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = CourseSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Delete method not allowed'})
#         try:
#             instance = Course.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Objects dont exist'})
#         instance.delete()
#         return Response({'post': 'delete post ' + str(pk)})
#
#

# class CourseAPIView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer