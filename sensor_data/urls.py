
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/data/', SensorDataListAPIView.as_view(), name='api-data'),
    path('filtered-data/', FilteredSensorView.as_view(), name='filtered-data'),
]
