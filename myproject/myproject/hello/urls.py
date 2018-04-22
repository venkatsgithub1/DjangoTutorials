# urls.py file in hello app.
from django.urls import path, include

# import views from same directory
from . import views

urlpatterns = [
    path('', views.index, name="index")
]