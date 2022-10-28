from django.urls import path
from . import views

app_name = "punto1"
urlpatterns = [
    path("", views.index, name="index")  
]