from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    
    