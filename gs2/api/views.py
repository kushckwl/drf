import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'create successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
           


