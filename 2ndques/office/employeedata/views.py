from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from employeedata.serializers import ManagerSerializer
from employeedata.models import Employee,Manager


class ManagerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]

