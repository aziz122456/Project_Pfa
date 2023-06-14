"""Project_Pfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


urlpatterns = [

path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('create_user/', CreateUserAPIView.as_view(), name='CreateUserAPIView'),
path('create_technician/', CreateTechnicianAPIView.as_view(), name='CreateUserAPIView'),
path('create_ticket/', CreateTicketView.as_view(), name='CreateTicketView'),
path('create_machine/',AddMachineView.as_view(), name='AddMachineView'),
path('create_machineFmily/',AddMachineFamilyView.as_view(), name='AddMachineFamilyView'),
path('take_tiket/',TakeTicketView.as_view(), name='TakeTicketView'),
path('tickets/delete/',DeleteTicketView.as_view(), name='delete-ticket'),
path('tickets/', TicketListAPIView.as_view(), name='ticket-list'),
path('machines/', MachineListAPIView.as_view(), name='machine-list'),
path('machine_familyList/', MachineFamilyListAPIView.as_view(), name='machineFamilyList'),
path('close_ticke/', CloseTicketView.as_view(), name='CloseTicke'),
path('filter_tickets_By_Status/', FilterTicketsByStatusView.as_view(), name='filter_tickets_By_Status'),
path('filter_tickets_By_Status/', FilterTicketsByStatusView.as_view(), name='filter_tickets_By_Status'),
path('filter_Technician_Tickets/', TechnicianTicketsView.as_view(), name='filter_Technician_Tickets'),
path('role/',RoleView.as_view(), name='role') ,

]
