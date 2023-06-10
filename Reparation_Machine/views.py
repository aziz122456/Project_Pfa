from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth.models import User
from Reparation_Machine.models import CustomUser
class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user.role = 'admin'  # Update the user's role to 'admin'
        user.save()
        data = {
            'message': 'Hello, world!',
            'role': request.user.role 
        }
        return Response(data)
    
    
class CreateUserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = 'user'
        # Create a new user object
        user = CustomUser.objects.create_user(username=username, password=password, email=email)
        user.role = role
        user.save()

        # Perform any additional operations or validations as needed

        return Response({'message': 'User created successfully'})
    
class CreateTechnicianAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = 'technician'
        # Create a new user object
        user = CustomUser.objects.create_user(username=username, password=password, email=email)
        user.role = role
        user.save()

        # Perform any additional operations or validations as needed

        return Response({'message': 'User created successfully'})    
    
    