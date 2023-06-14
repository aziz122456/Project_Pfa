from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from copy import deepcopy
from .models import MachineFamily, Ticket
from django.utils import timezone
from Reparation_Machine.models import CustomUser, Machine, StutType
from .serializers import TicketSerializer, MachineSerializer, MachineFamilySerializer


# Create_User_API_View
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
        return Response({'message': 'User created successfully'})


# Create_Technician_API_View
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
        return Response({'message': 'User created successfully'})


# Create_Ticket_API_View
class CreateTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mutable_data = deepcopy(request.data)
        mutable_data["utilisateur"] = request.user.id
        mutable_data["issueDate"] = timezone.now().date().strftime("%Y-%m-%d")
        serializer = TicketSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# take_Take_Ticket_View
class TakeTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            ticket = Ticket.objects.get(id=request.data.get('id'))
        except Ticket.DoesNotExist:
            return Response({'message': 'Ticket not found'}, status=404)
        ticket.technicien = request.user
        ticket.status = StutType.IN_PROGRESS
        if request.user.role != 'technician':
            return Response({'message': 'You are not a technician'}, status=404)
        ticket.save()
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)


# Add_Machine_View
class AddMachineView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mutable_data = deepcopy(request.data)
        mutable_data["start"] = timezone.now().date().strftime("%Y-%m-%d")
        serializer = MachineSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Add_Machine_Family_View
class AddMachineFamilyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MachineFamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Delete_Ticket_View
class DeleteTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'technician':
            return Response({'message': 'You are not a technician'}, status=404)
        try:
            ticket = Ticket.objects.get(id=request.data.get('id'))
        except Ticket.DoesNotExist:
            return Response({'message': 'Ticket not found'}, status=404)
        ticket.delete()
        return Response({'message': 'Ticket deleted'}, status=200)


# TicketListAPIView
class TicketListAPIView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


# MachineListAPIView
class MachineListAPIView(APIView):
    def get(self, request):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)


# MachineFamilyListAPIView
class MachineFamilyListAPIView(APIView):
    def get(self, request):
        machinefamily = MachineFamily.objects.all()
        serializer = MachineFamilySerializer(machinefamily, many=True)
        return Response(serializer.data)


# CloseTicketView
class CloseTicketView(APIView):
    def post(self, request):
        try:
            try:
                ticket = Ticket.objects.get(id=request.data.get('id'))
            except Ticket.DoesNotExist:
                return Response({'message': 'Ticket not found'}, status=404)
            if ticket.technicien.id != request.user.id:
                return Response({'message': 'Ticket Not Yours.'})
            mutable_data = deepcopy(request.data)
            mutable_data["closeDate"] = timezone.now().date().strftime("%Y-%m-%d")
            ticket.observation = request.data.get('observation')
            ticket.status = StutType.CLOSED
            ticket.save()
            return Response({'message': 'Ticket closed successfully.'})
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not found.'}, status=404)


# FilterTicketsByStatusView
class FilterTicketsByStatusView(APIView):
    def get(self, request):
        status = request.data.get('status')
        if not status:
            return Response({'error': 'Status is required in the request body.'}, status=400)

        sort_by_issue_date = request.data.get('sort_by_issue_date', False)

        tickets = Ticket.objects.filter(status=status)

        if sort_by_issue_date:
            tickets = tickets.order_by('issueDate')

        serializer = TicketSerializer(tickets, many=True)

        return Response({'tickets': serializer.data})


# TechnicianTicketsView
class TechnicianTicketsView(APIView):
    def get(self, request):
        tickets = Ticket.objects.filter(technicien=request.user.id)
        serializer = TicketSerializer(tickets, many=True)
        return Response({'tickets': serializer.data})


# RoleView
class RoleView(APIView):
    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        return Response({'tickets': user.role}) 
