from django.urls import path
from ubiot.views import index

urlpatterns = [
    path("", index, name="index")
]