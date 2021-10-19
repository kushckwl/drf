from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        print(instance.name)
        instance.name = validate_data.get('name', instance.name)   
        print(instance.name) 
        instance.roll = validate_data.get('roll', instance.roll)   
        instance.city = validate_data.get('city', instance.city)  
        instance.save()
        return instance 