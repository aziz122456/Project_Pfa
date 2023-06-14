from rest_framework import serializers
from .models import Ticket ,CustomUser ,Machine ,MachineFamily

class TicketSerializer(serializers.ModelSerializer):
    issueDate = serializers.DateField(format="%Y-%m-%d")
    closeDate = serializers.DateField(format="%Y-%m-%d",required=False, allow_null=True)
    technicien = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False)
    machine = serializers.PrimaryKeyRelatedField(queryset=Machine.objects.all(), required=False)
    class Meta:
        model = Ticket
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id','start', 'machineFamily']
        
class MachineFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineFamily
        fields = '__all__'        
