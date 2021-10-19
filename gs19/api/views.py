from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    