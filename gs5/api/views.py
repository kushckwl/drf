from django.shortcuts import render
import io
import requests

from requests.api import delete, request
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt, name = 'dispatch')
class StudentAPI(View):
    def get(self, request,*args, **kwargs):
         json_data = request.body
         stream = io.BytesIO(json_data)
         pythondata = JSONParser().parse(stream)
         id = pythondata.get('id', None)
         if id is not None:
             stu = Student.objects.get(id=id)
             serializer = StudentSerializer(stu)
             json_data = JSONRenderer().render(serializer.data)
             return HttpResponse(json_data, content_type='application/json')

         stu = Student.objects.all()
         serializer = StudentSerializer(stu,  many=True)
         json_data = JSONRenderer().render(serializer.data)
         return HttpResponse(json_data, content_type='application/json')
    
    def post(self,request,*args, **kwargs):
         json_data = request.body
         stream = io.BytesIO(json_data)
         parsed_data = JSONParser().parse(stream)
         serializer = StudentSerializer(data = parsed_data)
         if serializer.is_valid():
             serializer.save()
             res = {'msg':'Data created'}
             json_data = JSONRenderer().render(res)
             return HttpResponse(json_data, content_type='application/json')
         json_data = JSONRenderer().render(serializer.errors)
         return HttpResponse(json_data, content_type='application/json')

    def put(self,request,*args, **kwargs):
         json_data = request.body
         stream = io.BytesIO(json_data)
         parsed_data = JSONParser().parse(stream)
         id = parsed_data.get('id')
         stu = Student.objects.get(id=id)
         serializer = StudentSerializer(stu, data = parsed_data, partial = True)
         if serializer.is_valid():
             serializer.save()
             res = {'msg': 'updated successfully'}
             json_data = JSONRenderer().render(res)
             return HttpResponse(json_data, content_type='application/json')
         json_data = JSONRenderer().render(serializer.errors)
         return HttpResponse(json_data, content_type='application/json')
   

    def delete(self,request,*args, **kwargs):
         json_data = request.body
         stream = io.BytesIO(json_data)
         parsed_data = JSONParser().parse(stream)
         id = parsed_data.get('id')
         stu = Student.objects.get(id = id)
         stu.delete()
         res = {'msg': 'Data Deleted'}
         json_data = JSONRenderer().render(res)
         return HttpResponse(json_data, content_type='application/json')




    

   
    
    
  
    
   


