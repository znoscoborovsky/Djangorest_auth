from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view



class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url

    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
    
    def get(self, *args, **kwargs):
        users =  User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
