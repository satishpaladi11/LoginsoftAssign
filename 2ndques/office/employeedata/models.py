from django.db import models

class Manager(models.Model):
    manager_name = models.CharField(max_length=100)

class Employee(models.Model):
    manager = models.ForeignKey(Manager,related_name='emp_set', on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    