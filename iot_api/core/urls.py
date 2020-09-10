from .views import SensorReadingList
from django.urls import path

urlpatterns = [
    path('',SensorReadingList.as_view())
]
