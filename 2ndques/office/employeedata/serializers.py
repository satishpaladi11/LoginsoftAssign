from django.contrib.auth.models import User, Group
from rest_framework import serializers
from employeedata.models import Employee,Manager


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id','employee_name']


class ManagerSerializer(serializers.ModelSerializer):
    user = EmployeeSerializer(read_only=True, source="emp_set", many=True)
    class Meta:
        model = Manager
        fields = ['user','manager_name']