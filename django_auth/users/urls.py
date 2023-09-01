from django.urls import path
from .views import CreateUserAPIView
import users

urlpatterns = [

    path('create/', CreateUserAPIView.as_view()),
]
