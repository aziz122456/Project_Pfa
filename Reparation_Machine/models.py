from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('technician', 'Technician'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        attributes = vars(self)
        attributes_string = ', '.join([f"{key}: {value}" for key, value in attributes.items()])
        return f"CustomUser({attributes_string})"


class LevelType(models.TextChoices):
    LOW = 'LOW', 'Pane Low'
    NORMAL = 'NORMAL', 'Pane Normal'
    URGENT = 'URGENT', 'Pane Urgent'


class StutType(models.TextChoices):
    OPEN = 'OPEN', 'Ticket Opened'
    CLOSED = 'CLOSED', 'Ticket Closed'
    IN_PROGRESS = 'IN_PROGRESS', 'ticket in progress'


class MachineFamily(models.Model):
    nomMachine = models.TextField(max_length=20, default='')

    class Meta:
        db_table = 'Machine Family'

    def __str__(self):
        attributes = vars(self)
        attributes_string = ', '.join([f"{key}: {value}" for key, value in attributes.items()])
        return f"MachineFamily({attributes_string})"


class Machine(models.Model):
    id = models.CharField(max_length=255,default='',primary_key=True)
    start = models.DateField()
    machineFamily = models.ForeignKey(MachineFamily, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Machine'

    def __str__(self):
        attributes = vars(self)
        attributes_string = ', '.join([f"{key}: {value}" for key, value in attributes.items()])
        return f"Machine({attributes_string})"


class Ticket(models.Model):

    issueDate = models.DateField(null=True)
    closeDate = models.DateField(null=True)
    level = models.CharField(max_length=30, choices=LevelType.choices, default=LevelType.NORMAL)
    titel = models.CharField(max_length=30, default='')
    observation = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=1000, default='')
    status = models.CharField(max_length=20, choices=StutType.choices, default=StutType.OPEN)
    technicien = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tickets_technicien',null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tickets_user')

    class Meta:
        db_table = 'Ticket'

    def __str__(self):
        attributes = vars(self)
        attributes_string = ', '.join([f"{key}: {value}" for key, value in attributes.items()])
        return f"Ticket({attributes_string})"
