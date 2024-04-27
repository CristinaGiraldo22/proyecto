from .models import Employee
from rest_framework import serializers 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'identification','name', 'last_name','email','salary', 'is_activate')
        
        # read_only_fields = ('id',)