from django.urls import path
from myapp.views import helloWorld

urlpatterns = [
    path('/hello-world', helloWorld, name="helloWorld")
]