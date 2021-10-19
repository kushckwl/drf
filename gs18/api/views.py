from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

class StudentModelReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer