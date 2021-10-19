from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status

# Create your views here.

class StudentApi(APIView):
    def get(self,request,pk=None, formate=None):
         id = pk
         if id is not None:
             stu = Student.objects.get(pk=id)
             serializer = StudentSerializer(stu)
             return Response(serializer.data)

         stu = Student.objects.all()
         serializer = StudentSerializer(stu, many=True)
         return Response(serializer.data)    

    def post(self,request,formate=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def put(self,request,pk=None, formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def patch(self,request,pk=None, formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk=None, formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})    

