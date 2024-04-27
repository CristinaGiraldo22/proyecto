from  rest_framework import viewsets, permissions
from .models import Employee
from .serializers import EmployeeSerializer


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permissions_class =[permissions.AllowAny]   
    serializer_class = EmployeeSerializer  
    