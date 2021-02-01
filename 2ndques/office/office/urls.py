from django.urls import include, path
from rest_framework import routers
from employeedata import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'employees', views.ManagerViewSet,basename='Manager')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]